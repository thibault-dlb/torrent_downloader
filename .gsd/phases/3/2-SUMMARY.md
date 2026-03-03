# Plan 3.2 Summary: Cycle de vie VLC et Nettoyage Avancé

## Ce qui a été fait
- Dans `ui.py`, la fonction `manage_download_progress` a été mise à jour pour accepter optionnellement le processus VLC (`vlc_process`).
- Une surveillance active a été ajoutée : si VLC est fermé par l'utilisateur (`vlc_process.poll() is not None`), la barre de progression s'interrompt proprement et libère le téléchargement.
- Dans `cli.py`, la suppression des fichiers de cache a été renforcée. Windows conservant un verrou sur le fichier vidéo quelques secondes après la fermeture du lecteur, une boucle `retry` avec `time.sleep(2)` espacée de 3 essais a été implémentée autour de `shutil.rmtree()` / `unlink()`.

## Vérification
- Le comportement de la barre de progression gère l'annulation.
- Le log `⚠️ VLC a été fermé. Interruption du téléchargement...` s'affichera correctement.

## État
- **Status :** TERMINÉ ✓
- **Phase 3 :** COMPLÈTE ✓
