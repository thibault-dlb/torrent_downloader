# SPEC.md — Spécification du Projet

> **Status**: `FINALIZED`

## Vision
Transformer CineCLI d'un simple navigateur de films en un client torrent complet capable de streaming. L'utilisateur peut rechercher un film, le visionner en direct via VLC (grâce au téléchargement séquentiel) ou le télécharger de manière permanente, le tout avec une interface terminale moderne et fluide.

## Objectifs
1. **Intégration de libtorrent** : Remplacer l'ouverture externe par un moteur torrent interne gérant le téléchargement séquentiel.
2. **Streaming & Lecture** : Permettre le visionnage immédiat dans VLC pendant le téléchargement.
3. **Gestion Hybride** : Offrir trois modes : "Regarder" (cache temporaire), "Télécharger" (permanent), et "Les deux".
4. **Configuration Intuitive** : Gérer les dossiers de téléchargement et la détection de VLC de manière persistante.

## Hors de Portée (Non-Goals)
- Support du transcodage vidéo (lecture directe du fichier source uniquement).
- Gestion de bibliothèque de films (historique de lecture/téléchargement).
- Interface Graphique (GUI) — le projet reste 100% CLI.

## Utilisateurs
Utilisateurs de terminal souhaitant une expérience "Popcorn Time" légère, sans quitter leur ligne de commande, avec un contrôle total sur l'emplacement des fichiers.

## Contraintes
- **Techniques** : Python 3.9+, `libtorrent` pour la logique torrent, `VLC` installé sur le système.
- **Plateforme** : Initialement optimisé pour Windows (spécifié par l'OS de l'utilisateur), mais structuré pour être portable.
- **Performance** : Le téléchargement séquentiel doit être assez performant pour éviter les saccades dans VLC.

## Critères de Succès
- [ ] L'utilisateur peut configurer son dossier permanent au premier lancement.
- [ ] Le streaming démarre dans VLC dès que les premières pièces sont disponibles.
- [ ] Les fichiers temporaires sont supprimés automatiquement à la fermeture de VLC.
- [ ] Une barre de progression `Rich` affiche l'état du téléchargement en temps réel.
