---
phase: 2
plan: 1
wave: 1
---

# Plan 2.1: Intégration de Libtorrent & Logique Séquentielle

## Objectif
Remplacer la logique actuelle de gestion des magnets par un moteur `libtorrent` interne capable de gérer le téléchargement séquentiel.

## Context
- .gsd/SPEC.md
- .gsd/phases/2/RESEARCH.md
- cinecli/cinecli/magnets.py

## Tasks

<task type="auto">
  <name>Création du moteur torrent (downloader.py)</name>
  <files>cinecli/cinecli/downloader.py</files>
  <action>
    - Créer `downloader.py` pour encapsuler la logique `libtorrent`.
    - Implémenter une classe `TorrentDownloader` qui gère la session et l'ajout de magnets.
    - Activer `set_sequential_download(True)`.
    - Ajouter une méthode pour identifier le fichier vidéo principal dans le torrent.
  </action>
  <verify>python -c "import libtorrent as lt; print(lt.version)"</verify>
  <done>La structure de base pour télécharger via libtorrent est en place.</done>
</task>

<task type="auto">
  <name>Mise à jour de magnets.py</name>
  <files>cinecli/cinecli/magnets.py</files>
  <action>
    - Refactoriser `magnets.py` pour utiliser `TorrentDownloader` au lieu de déléguer systématiquement au navigateur ou à Transmission.
    - Conserver la rétrocompatibilité pour Transmission si activé, mais préparer le terrain pour le mode interne.
  </action>
  <verify>python -c "from cinecli.magnets import build_magnet; print(build_magnet('abc', 'test'))"</verify>
  <done>Magnets.py est prêt à utiliser le nouveau downloader.</done>
</task>

## Success Criteria
- [ ] Le package `libtorrent` est importable.
- [ ] Un magnet peut être converti en torrent actif dans une session libtorrent locale.
