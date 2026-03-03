---
phase: 3
plan: 1
wave: 1
---

# Plan 3.1: Intégration avancée de VLC et Buffer de Streaming

## Objectif
Permettre une lecture vidéo fluide en définissant un pre-buffering et en priorisant les pièces clés du fichier torrent, afin d'éviter que VLC ne crashe au lancement.

## Context
- .gsd/SPEC.md
- .gsd/ROADMAP.md
- .gsd/phases/3/RESEARCH.md
- cinecli/cinecli/downloader.py
- cinecli/cinecli/cli.py

## Tasks

<task type="auto">
  <name>Priorisation des pièces</name>
  <files>cinecli/cinecli/downloader.py</files>
  <action>
    - Dans `downloader.py`, ajouter une méthode `prioritize_streaming_pieces()` appelée après la récupération des métadonnées.
    - Identifier le fichier principal et ses "piece index" associés.
    - Mettre la `piece_priority` à 7 (maximum) pour le premier 5% et le dernier 1% des pièces du fichier vidéo (pour les headers MP4/MKV).
  </action>
  <verify>python -c "from cinecli.downloader import TorrentDownloader; print(hasattr(TorrentDownloader, 'prioritize_streaming_pieces'))"</verify>
  <done>Le gestionnaire de téléchargement applique correctement les priorités pour un streaming optimal.</done>
</task>

<task type="auto">
  <name>Pre-buffering & Lancement différé</name>
  <files>cinecli/cinecli/cli.py, cinecli/cinecli/ui.py</files>
  <action>
    - Actuellement le `subprocess.Popen` de VLC est lancé instantanément après les métadonnées.
    - Modifier le flux dans `cli.py` ou `ui.py` (ou créer une boucle d'attente) pour patienter jusqu'à ce que 2% ou 5 Mo de la vidéo soient téléchargés *avant* de lancer VLC.
    - Afficher un statut "[cyan]Mise en mémoire tampon ([x]% / 2%)[/cyan]" dans `manage_download_progress` ou avant.
  </action>
  <verify>Lancer cinecli sur un magnet "Watch" et vérifier visuellement l'attente du buffer avant l'ouverture de VLC.</verify>
  <done>VLC attend que le fichier contienne assez de données pour démarrer la lecture sans erreur.</done>
</task>

## Success Criteria
- [ ] Une vidéo test (ex: Big Buck Bunny ou film libre) se lance dans VLC et joue les premières secondes sans crasher.
- [ ] La CLI affiche un message de mise en cache avant l'apparition de la fenêtre VLC.
