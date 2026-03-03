# ROADMAP.md

> **Current Phase**: Phase 1: Foundation & Specs
> **Milestone**: v0.2.0 (Streaming Client)

## Incontournables (depuis SPEC)
- [ ] Moteur libtorrent fonctionnel
- [ ] Lecture séquentielle dans VLC
- [ ] Nettoyage automatique du cache

## Phases

### Phase 1: Socle Technique & Configuration
**Status**: 🚧 In Progress
**Objectif**: Mettre à jour la configuration et préparer l'environnement libtorrent.
**Exigences**: REQ-03, REQ-05, REQ-09

### Phase 2: Moteur Torrent (Libtorrent)
**Status**: ⬜ Not Started
**Objectif**: Implémenter la logique de téléchargement séquentiel et les barres de progression.
**Exigences**: REQ-01, REQ-02, REQ-08

### Phase 3: Intégration VLC & Streaming
**Status**: ⬜ Not Started
**Objectif**: Lancer VLC sur le fichier en cours de téléchargement et gérer les processus.
**Exigences**: REQ-04, REQ-06

### Phase 4: Gestion des Modes & Nettoyage
**Status**: ⬜ Not Started
**Objectif**: Finaliser les modes (Regarder/Télécharger/Les deux) et la gestion des fichiers.
**Exigences**: REQ-07

### Phase 5: Polissage & Validation
**Status**: ⬜ Not Started
**Objectif**: Tests de bout en bout et gestion des erreurs de connexion/disque.
