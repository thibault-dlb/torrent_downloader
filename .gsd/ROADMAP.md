# ROADMAP.md

> **Current Phase**: Phase 2: Moteur Torrent (Libtorrent)
> **Milestone**: v0.2.0 (Streaming Client)

## Incontournables (depuis SPEC)
- [ ] Moteur libtorrent fonctionnel
- [ ] Lecture séquentielle dans VLC
- [ ] Nettoyage automatique du cache

## Phases

### Phase 1: Socle Technique & Configuration
**Status**: ✅ Complete
**Objective**: Mettre à jour la configuration et préparer l'environnement libtorrent.
**Requirements**: REQ-03, REQ-05, REQ-09

## Current Position
- **Phase**: 3 (completed)
- **Task**: Phase 3 execution verified
- **Status**: Ready for Phase 4

## Next Steps
1. /plan 4 (Gestion des Modes & Nettoyage)

### Phase 2: Moteur Torrent (Libtorrent)
**Status**: ✅ Complete
**Objective**: Implémenter la logique de téléchargement séquentiel et les barres de progression.
**Exigences**: REQ-01, REQ-02, REQ-08

### Phase 3: Intégration VLC & Streaming
**Status**: ✅ Complete
**Objective**: Lancer VLC sur le fichier en cours de téléchargement et gérer les processus.
**Exigences**: REQ-04, REQ-06

### Phase 4: Gestion des Modes & Nettoyage
**Status**: 🚧 In Progress
**Objective**: Finaliser les modes (Regarder/Télécharger/Les deux) et la gestion des fichiers.
**Exigences**: REQ-07

### Phase 5: Polissage & Validation
**Status**: ⬜ Not Started
**Objectif**: Tests de bout en bout et gestion des erreurs de connexion/disque.
