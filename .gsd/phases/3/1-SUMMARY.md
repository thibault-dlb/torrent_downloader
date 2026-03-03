# Plan 3.1 Summary: Pre-buffering & Priorisation VLC

## Ce qui a été fait
- Ajout de la méthode `prioritize_streaming_pieces()` dans `downloader.py` pour forcer `libtorrent` à télécharger en priorité absolue (niveau 7) les premiers 5% et le dernier 1% du fichier vidéo. Ceci garantit que VLC dispose des headers (ex: atomes MOOV pour MP4) dès le lancement.
- Modification de `start_torrent_action` dans `cli.py` :
    - Ajout d'une boucle d'attente (Pre-buffering) qui met en pause le lancement de VLC jusqu'à ce que `libtorrent` ait téléchargé au moins 2% du fichier ou qu'un délai de 15 secondes se soit écoulé.
    - Ajout de logs interactifs avec `rich` expliquant l'attente à l'utilisateur.

## Vérification
- La logique de calcul des pièces a été ajoutée et testée syntaxiquement.
- La boucle d'attente utilise correctement `time.time()` pour un timeout non-bloquant.

## État
- **Status :** TERMINÉ ✓
- **Suivant :** Plan 3.2 (Cycle de vie)
