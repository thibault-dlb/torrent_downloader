# Decisions

> Registre des décisions architecturales et techniques.

## Phase 1 Decisions

**Date:** 2026-03-03

### Scope
- **Configuration** : Conserver le format TOML. Emplacement : `~/.config/cinecli/config.toml`.
- **Dossiers** : le dossier permanent est configuré à la première utilisation. Le dossier temporaire est géré automatiquement sans intervention utilisateur (cache).
- **Validation** : Vérifier les permissions d'écriture sur le dossier permanent choisi.

### Approach
- **Détection VLC** : Recherche automatique dans les chemins standards (Program Files) et via le registre Windows.
- **Commande de config** : Ajout de `cinecli config --path <path>` pour modifier le dossier de destination.

### Constraints
- **Windows Only** : Optimisation exclusive pour l'écosystème Windows.
- **Zéro interaction superflue** : Le téléchargement temporaire est invisible pour l'utilisateur.
