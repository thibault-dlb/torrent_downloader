# Plan 2.2 Summary: UI Progress & Gestion du téléchargement

## Ce qui a été fait
- Implémentation d'une barre de progression interactive avec `rich.progress` dans `ui.py` (`manage_download_progress`).
- Intégration complète du cycle de vie dans `cli.py` (fonction `start_torrent_action`) :
    - 3 options offertes à l'utilisateur : Regarder (temp), Télécharger (permanent), Regarder et Télécharger.
    - Lancement de `vlc.exe` via `subprocess.Popen` si le mode streaming est sélectionné.
    - Attente de la fin du téléchargement avec barre d'avancement.
    - Nettoyage du dossier/fichier vidéo temporaire (via `shutil.rmtree` / `unlink`) lorsque le téléchargement et le stream sont terminés (action 1).

## Vérification
- Le prompt des 3 options s'affiche correctement au lieu de la simple demande magnet/torrent.
- La syntaxe du fichier a été validée.

## État
- **Status :** TERMINÉ ✓
- **Phase 2 :** COMPLÈTE ✓
