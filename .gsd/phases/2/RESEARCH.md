# Research Phase 2: Libtorrent & Downloading Séquentiel

## Moteur Libtorrent

### Installation
`pip install libtorrent` est le standard. Sur Windows, il est généralement pré-compilé.

### Configuration du Téléchargement Séquentiel
Dans `libtorrent`, le mode séquentiel peut être activé par torrent. Cela force le moteur à prioriser les pièces dans l'ordre de leur index.

```python
import libtorrent as lt

# Initialisation session
ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})

# Ajout d'un torrent/magnet
params = lt.parse_magnet_uri(magnet_link)
params.save_path = save_path
handle = ses.add_torrent(params)

# Activer le mode séquentiel
handle.set_sequential_download(True)

# Important : On peut aussi prioriser manuellement les premières pièces
# pour garantir que VLC puisse ouvrir le fichier rapidement.
handle.piece_priority(0, 7) # Priorité maximale pour la pièce 0
```

### Surveillance de l'état
On utilise `handle.status()` pour obtenir les informations de vitesse, progression et nombre de seeds.

## Barre de Progression avec Rich

Rich propose un composant `Progress` très performant qui supporte plusieurs barres en parallèle.
Pour CineCLI, une barre unique avec :
- Nom du fichier
- Pourcentage
- Vitesse (Download/Upload)
- Temps restant (ETA)

```python
from rich.progress import Progress, TextColumn, BarColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn

with Progress(
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(),
    "[progress.percentage]{task.percentage:>3.1f}%",
    DownloadColumn(),
    TransferSpeedColumn(),
    TimeRemainingColumn(),
) as progress:
    task_id = progress.add_task("download", filename="Movie.mp4", total=total_size)
    # ... update loop ...
```

## Gestion des fichiers dans un torrent
Un torrent peut contenir plusieurs fichiers (film, sous-titres, nfo).
- Il faut identifier le fichier vidéo principal (plus gros fichier).
- On peut mettre la priorité de téléchargement à 0 pour les fichiers inutiles.
