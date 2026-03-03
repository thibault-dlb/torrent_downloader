---
phase: 2
plan: 2
wave: 1
---

# Plan 2.2: UI Progress & Gestion du téléchargement

## Objectif
Afficher une barre de progression interactive pour le téléchargement et gérer le cycle de vie du processus (metadata, download, stop).

## Context
- .gsd/SPEC.md
- .gsd/phases/2/RESEARCH.md
- cinecli/cinecli/downloader.py
- cinecli/cinecli/ui.py

## Tasks

<task type="auto">
  <name>UI Progress avec Rich</name>
  <files>cinecli/cinecli/ui.py</files>
  <action>
    - Ajouter `show_progress(handle, filename)` qui utilise `rich.progress`.
    - Gérer l'affichage de la vitesse de téléchargement, progression (%) et ETA.
    - Créer un callback ou une boucle pour mettre à jour l'UI régulièrement.
  </action>
  <verify>python -c "from cinecli.ui import show_progress; print('show_progress defined')"</verify>
  <done>La barre de progression Rich s'affiche et se met à jour correctement.</done>
</task>

<task type="auto">
  <name>Processus de téléchargement complet</name>
  <files>cinecli/cinecli/downloader.py</files>
  <action>
    - Implémenter une méthode `wait_for_metadata()` pour récupérer les informations du torrent avant de démarrer.
    - Gérer l'arrêt propre de la session (saving resume data, etc.).
    - Gérer le téléchargement vers le dossier temporaire (si mode "Watch").
  </action>
  <verify>python -c "from cinecli.downloader import TorrentDownloader; print('Downloader ready for metadata')"</verify>
  <done>On peut lancer un téléchargement vers un dossier arbitraire et suivre sa progression.</done>
</task>

## Success Criteria
- [ ] Une barre de progression réelle s'affiche lors d'un test de magnet.
- [ ] La vitesse de téléchargement est affichée dynamiquement.
