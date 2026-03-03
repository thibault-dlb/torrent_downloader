from rich.table import Table
from rich.console import Console
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
)
import time

console = Console()

def show_movies(movies):
    table = Table(title="🎬 Search Results")

    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Title", style="bold")
    table.add_column("Year", justify="center")

    for movie in movies:
        table.add_row(
            str(movie["id"]),
            movie["title"],
            str(movie["year"]),
        )

    console.print(table)

from rich.panel import Panel

def show_movie_details(movie):
    description = (
        movie.get("summary")
        or movie.get("description_full")
        or "No description available."
    )

    text = (
        f"[bold]{movie['title']} ({movie['year']})[/bold]\n\n"
        f"🎭 Genres: {', '.join(movie.get('genres', []))}\n\n"
        f"{description}"
    )
    console.print(Panel(text, title="🎬 Movie Details", expand=False))


def show_torrents(torrents):
    table = Table(title="🧲 Available Torrents")

    table.add_column("Index", justify="center")
    table.add_column("Quality")
    table.add_column("Size")
    table.add_column("Seeds", justify="center")
    table.add_column("Peers", justify="center")

    for idx, torrent in enumerate(torrents):
        table.add_row(
            str(idx),
            torrent["quality"],
            torrent["size"],
            str(torrent["seeds"]),
            str(torrent["peers"]),
        )

    console.print(table)


def manage_download_progress(handle, filename, vlc_process=None):
    """
    Affiche une barre de progression pour un téléchargement libtorrent.
    Si vlc_process est fourni, surveille son état. S'il est fermé, on s'arrête.
    """
    console.print()  # Saut de ligne avant la barre pour l'isoler
    
    with Progress(
        TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.1f}%",
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
        console=console,
    ) as progress:
        task_id = progress.add_task("download", filename=filename, total=100)
        
        while not handle.is_finished():
            # Si le lecteur VLC a été fermé par l'utilisateur, on arrête tout
            if vlc_process and vlc_process.poll() is not None:
                console.print("\n[yellow]⚠️ VLC a été fermé. Interruption du téléchargement...[/yellow]")
                break
                
            s = handle.status()
            progress.update(
                task_id,
                completed=s.progress * 100,
                description=f"Statut: {s.state}"
            )
            
            # Si on a fini ou presque (libtorrent peut s'arrêter à 99.9%)
            if s.progress >= 1.0:
                break
                
            time.sleep(0.5)
        
        # On ne met à 100% que si on n'a pas été interrompu
        if handle.is_finished() or handle.status().progress >= 1.0:
            progress.update(task_id, completed=100)

    console.print()  # Saut de ligne après la barre pour la clarté
