---
phase: 3
plan: 2
wave: 1
---

# Plan 3.2: Cycle de vie VLC et Nettoyage Avancé

## Objectif
Gérer robuste-ment la fermeture de VLC, l'interruption du téléchargement si VLC est fermé, et le nettoyage des fichiers temporaires, y compris en cas de crash brutal ou d'erreur `PermissionError` (fichier verrouillé par VLC sous Windows).

## Context
- .gsd/SPEC.md
- .gsd/ROADMAP.md
- .gsd/phases/3/RESEARCH.md
- cinecli/cinecli/cli.py

## Tasks

<task type="auto">
  <name>Surveillance du processus VLC</name>
  <files>cinecli/cinecli/cli.py</files>
  <action>
    - Dans `start_torrent_action`, au lieu d'une simple boucle `while not handle.is_finished()`, on doit surveiller l'état de `vlc_process` si l'option 1 (Regarder) a été choisie.
    - Si l'utilisateur ferme VLC, alors `vlc_process.poll()` ne sera plus `None`. Dans ce cas, interrompre immédiatement le téléchargement libtorrent s'il n'est pas fini, car il n'est plus utile.
  </action>
  <verify>Lancer un stream, fermer VLC à 10%. Le téléchargement doit s'arrêter et le cache se vider.</verify>
  <done>La fermeture de VLC interrompt le téléchargement temporaire proprement.</done>
</task>

<task type="auto">
  <name>Gestion robuste du nettoyage (Windows Locks)</name>
  <files>cinecli/cinecli/cli.py</files>
  <action>
    - Le nettoyage avec `shutil.rmtree` peut échouer sous Windows si le fichier est encore retenu par le processus système quelques millisecondes après la fermeture de VLC.
    - Ajouter une boucle de retry (3 essais avec `time.sleep(1)`) pour la suppression dans le bloc `except`.
    - Ajouter éventuellement un message amical ("Nettoyage du cache...").
  </action>
  <verify>Après la fermeture de VLC, le cache est supprimé sans laisser de stack trace moche à l'écran.</verify>
  <done>La suppression du cache temporaire est résiliente aux verrous Windows.</done>
</task>

## Success Criteria
- [ ] L'arrêt prématuré de VLC coupe le téléchargement inutile et nettoie le dossier.
- [ ] Le nettoyage du fichier à la fin ne génère pas de `PermissionError` sous Windows.
