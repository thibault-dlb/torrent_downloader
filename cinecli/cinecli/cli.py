import typer
from rich.prompt import Prompt
from rich.console import Console
from cinecli.config import load_config, save_config
from cinecli.utils import check_write_permission, find_vlc_path
from cinecli.downloader import TorrentDownloader
from cinecli.ui import manage_download_progress
from pathlib import Path
import subprocess
import shutil
import time


from cinecli.api import search_movies, get_movie_details
from cinecli.ui import (
    show_movies,
    show_movie_details,
    show_torrents,
)
from cinecli.magnets import (
    build_magnet,
    select_best_torrent,
)

# -------------------------------------------------
# App + Console
# -------------------------------------------------

app = typer.Typer(
    help="🎬 CineCLI — Browse and torrent movies from your terminal",
)
config_data = load_config()
console = Console()

@app.callback()
def main():
    """
    Vérifie la configuration au démarrage.
    """
    if not config_data.get("permanent_path"):
        console.print("[yellow]👋 Bienvenue dans CineCLI ![/yellow]")
        console.print("Il semble que ce soit votre premier lancement.")
        
        path = ""
        while not path:
            path = Prompt.ask("📂 Où souhaitez-vous enregistrer vos films téléchargés ? (Chemin complet)")
            if not check_write_permission(path):
                console.print("[red]❌ Chemin invalide ou sans permission d'écriture.[/red]")
                path = ""
        
        config_data["permanent_path"] = path
        
        if not config_data.get("vlc_path"):
            vlc = find_vlc_path()
            if vlc:
                console.print(f"[green]✅ VLC détecté : {vlc}[/green]")
                config_data["vlc_path"] = vlc
            else:
                config_data["vlc_path"] = Prompt.ask("🎬 Chemin vers l'exécutable VLC (vlc.exe)")
        
        save_config(config_data)
        console.print("[green]✨ Configuration sauvegardée ![/green]\n")

# -------------------------------------------------
# Config command
# -------------------------------------------------

@app.command("config")
def config_cmd(
    path: str = typer.Option(None, "--path", help="Changer le dossier de téléchargement permanent"),
    vlc: str = typer.Option(None, "--vlc", help="Changer le chemin de VLC"),
):
    """
    Gérer la configuration de CineCLI
    """
    updated = False
    
    if path:
        if check_write_permission(path):
            config_data["permanent_path"] = path
            console.print(f"[green]✅ Dossier permanent mis à jour : {path}[/green]")
            updated = True
        else:
            console.print("[red]❌ Permission d'écriture refusée sur ce dossier.[/red]")
            raise typer.Exit(code=1)
            
    if vlc:
        config_data["vlc_path"] = vlc
        console.print(f"[green]✅ Chemin VLC mis à jour : {vlc}[/green]")
        updated = True
        
    if updated:
        save_config(config_data)
    else:
        console.print("[cyan]Configuration actuelle :[/cyan]")
        for k, v in config_data.items():
            console.print(f"  [bold]{k}:[/bold] {v}")

# -------------------------------------------------
# Search command
# -------------------------------------------------

@app.command()
def search(
    query: list[str] = typer.Argument(..., help="Movie name to search for"),
    limit: int = typer.Option(10),
):
    search_query = " ".join(query)
    movies = search_movies(search_query, limit)


    if not movies:
        console.print("[red]❌ No movies found.[/red]")
        raise typer.Exit(code=1)

    show_movies(movies)

def start_torrent_action(movie_title: str, torrent: dict, action: str, config_data: dict):
    magnet = build_magnet(torrent["hash"], f"{movie_title} {torrent['quality']}")
    
    # 1: Regarder (temp), 2: Télécharger (perm), 3: Les deux (perm)
    is_streaming = action in ["1", "3"]
    is_permanent = action in ["2", "3"]
    
    save_path = config_data.get("permanent_path") if is_permanent else config_data.get("temp_path")
    
    console.print(f"\n[cyan]🚀 Démarrage du moteur torrent (Dossier: {save_path})...[/cyan]")
    downloader = TorrentDownloader(save_path)
    handle = downloader.add_magnet(magnet, sequential=is_streaming)
    
    console.print("[cyan]⏳ Récupération des métadonnées du torrent (Patientez)...[/cyan]")
    if not downloader.wait_for_metadata(60):
        console.print("[red]❌ Échec de la récupération des métadonnées (pas de sources ou problème réseau).[/red]")
        return
        
    main_file = downloader.get_main_file()
    if not main_file:
        console.print("[red]❌ Impossible d'identifier le fichier vidéo principal.[/red]")
        return
        
    downloader.prioritize_streaming_pieces()
        
    file_path = main_file["path"]
    full_path = str(Path(save_path) / file_path)
    
    vlc_process = None
    if is_streaming:
        vlc_path = config_data.get("vlc_path")
        if vlc_path and Path(vlc_path).exists():
            console.print("\n[cyan]⏳ Mise en mémoire tampon (pre-buffering)...[/cyan]")
            # Attendre 2% ou max 15 secondes pour le pre-buffering
            buffer_start = time.time()
            while not handle.is_finished():
                if handle.status().progress >= 0.02 or (time.time() - buffer_start) > 15:
                    break
                time.sleep(1)
                
            console.print(f"[green]🎬 Lancement de VLC pour la lecture en cours de téléchargement ![/green]")
            vlc_process = subprocess.Popen([vlc_path, full_path])
        else:
            console.print("[yellow]⚠️ Chemin de VLC invalide. Le téléchargement continue mais sans VLC.[/yellow]")
    
    console.print("\n[cyan]⬇️ Téléchargement en cours...[/cyan]")
    
    # Custom wait loop to monitor VLC if streaming
    if is_streaming and vlc_process:
        console.print("[yellow]💡 Conseil : Fermez VLC pour annuler le téléchargement temporaire.[/yellow]")
        manage_download_progress(handle, file_path, vlc_process)
    else:
        manage_download_progress(handle, file_path)
        
    console.print("[green]✅ Téléchargement terminé (ou interrompu) ![/green]")
    
    if action == "1":
        if vlc_process and vlc_process.poll() is None:
            console.print("[cyan]Attente de la fermeture de VLC pour nettoyage du cache temporaire...[/cyan]")
            vlc_process.wait()
        
        console.print("[cyan]🗑️ Suppression des fichiers temporaires...[/cyan]")
        
        # Retry loop for Windows file locks
        for _ in range(3):
            try:
                base_folder = Path(save_path) / Path(file_path).parts[0]
                if base_folder.is_dir():
                    shutil.rmtree(base_folder, ignore_errors=True)
                elif base_folder.is_file():
                    base_folder.unlink(missing_ok=True)
                console.print("[green]✨ Nettoyage terminé.[/green]")
                break
            except Exception:
                time.sleep(2)

# -------------------------------------------------
# Watch command
# -------------------------------------------------

@app.command()
def watch(movie_id: int):
    """
    Consulter les détails d'un film et choisir l'action (Regarder/Télécharger).
    """
    movie = get_movie_details(movie_id)

    show_movie_details(movie)

    torrents = movie.get("torrents", [])
    if not torrents:
        console.print("[red]❌ No torrents available.[/red]")
        raise typer.Exit(code=1)

    show_torrents(torrents)
    auto = typer.confirm("🎯 Auto-select best torrent?", default=True)

    if auto:
        torrent = select_best_torrent(torrents)
        typer.echo(
            f"🎯 Auto-selected torrent: {torrent['quality']} ({torrent['size']})"
        )
    else:
        index = typer.prompt(
            "Select torrent index",
            type=int
        )

        if index < 0 or index >= len(torrents):
            typer.echo("❌ Invalid torrent index")
            raise typer.Exit(code=1)

        torrent = torrents[index]



    console.print("\n[bold]Que souhaitez-vous faire ?[/bold]")
    console.print("  [cyan]1)[/cyan] Regarder le film (téléchargement temporaire)")
    console.print("  [cyan]2)[/cyan] Télécharger le film (dossier permanent)")
    console.print("  [cyan]3)[/cyan] Les deux : Regarder et télécharger (dossier permanent)")
    
    action = Prompt.ask(
        "Choix",
        choices=["1", "2", "3"],
        default="1",
    )

    start_torrent_action(movie["title"], torrent, action, config_data)
# -------------------------------------------------
# Interactive command
# -------------------------------------------------

@app.command()
def interactive():
    """
    Navigateur de films interactif avec gestion du streaming.
    """
    query = Prompt.ask("🔍 Search movies")

    movies = search_movies(query, limit=10)
    if not movies:
        console.print("[red]❌ No movies found.[/red]")
        raise typer.Exit()

    # Show movie list
    for idx, movie in enumerate(movies):
        console.print(
            f"[cyan][{idx}][/cyan] "
            f"{movie['title']} ({movie['year']}) "
        )

    movie_index = Prompt.ask(
        "Select movie index",
        choices=[str(i) for i in range(len(movies))]
    )

    movie_id = movies[int(movie_index)]["id"]

    movie = get_movie_details(movie_id)
    show_movie_details(movie)

    torrents = movie.get("torrents", [])
    if not torrents:
        console.print("[red]❌ No torrents available.[/red]")
        raise typer.Exit()

    show_torrents(torrents)

    torrent_index = Prompt.ask(
        "Select torrent index",
        choices=[str(i) for i in range(len(torrents))]
    )

    torrent = torrents[int(torrent_index)]

    console.print("\n[bold]Que souhaitez-vous faire ?[/bold]")
    console.print("  [cyan]1)[/cyan] Regarder le film (téléchargement temporaire)")
    console.print("  [cyan]2)[/cyan] Télécharger le film (dossier permanent)")
    console.print("  [cyan]3)[/cyan] Les deux : Regarder et télécharger (dossier permanent)")
    
    action = Prompt.ask(
        "Choix",
        choices=["1", "2", "3"],
        default="1",
    )

    start_torrent_action(movie["title"], torrent, action, config_data)

