# Research Phase 3: Intégration avancée de VLC et Streaming

## Priorisation des Pièces (Piece Prioritization)
Bien que `handle.set_sequential_download(True)` demande à libtorrent de télécharger les pièces dans l'ordre, VLC a besoin spécifiquement du début (headers) et souvent de la fin du fichier (si mp4/mkv avec l'index à la fin) pour commencer la lecture.

Dans `downloader.py`, il faudrait s'assurer que les premières et dernières pièces ont la priorité maximale.
```python
info = handle.get_torrent_info()
num_pieces = info.num_pieces()
# Prioritize first 5 pieces and last 5 pieces
for i in range(min(5, num_pieces)):
    handle.piece_priority(i, 7)
for i in range(max(0, num_pieces - 5), num_pieces):
    handle.piece_priority(i, 7)
```

## Buffer de Démarrage (Pre-buffering)
Actuellement, VLC est lancé *immédiatement* après la récupération des métadonnées. C'est risqué car le fichier sur le disque peut être vide (0 byte) et VLC va simplement crasher ou s'arrêter.
Il faut imposer un "pre-buffering". On attend qu'un minimum de téléchargement soit effectué (ex: 2% ou 5Mo) avant de faire le `subprocess.Popen` de VLC.

## VLC et le fichier bloqué (File Locking) sur Windows
Sous Windows, si libtorrent écrit dans un fichier, VLC peut parfois refuser de le lire s'il y a un conflit de verrouillage strict.
Heureusement, libtorrent gère ses accès disque de manière accommodante, mais il faut avertir l'utilisateur de ne pas quitter la fenêtre CLI pendant que VLC tourne en mode temp, car la CLI nettoie le fichier à la fermeture de VLC.

## Interface CLI de Streaming
La CLI devrait idéalement afficher "Streaming en cours... Quittez VLC pour arrêter." puis bloquer l'exécution (via `vlc_process.wait()`).
Pendant ce temps, la barre de téléchargement de Rich devrait continuer de se mettre à jour en arrière-plan (ce qu'elle fait déjà dans `manage_download_progress`).
