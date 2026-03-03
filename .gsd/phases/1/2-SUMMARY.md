# Plan 1.2 Summary: Commandes CLI & Initialisation

## Ce qui a été fait
- Mise à jour de `cinecli/cli.py` :
    - Ajout d'un callback `main()` pour détecter le premier lancement et proposer une configuration interactive (dossier permanent et VLC).
    - Ajout de la commande `cinecli config` pour visualiser et modifier les paramètres (`--path` et `--vlc`).
    - Validation des entrées utilisateur via `check_write_permission`.
    - Résolution des conflits de noms entre la variable `config` et la commande `config`.
- Intégration de la boucle de sauvegarde automatique lors de la première configuration.

## Vérification
- `python -m cinecli config` affiche correctement la configuration actuelle.
- Si `permanent_path` est vide, l'interpréteur Typer lance bien le prompt interactif.
- La commande met à jour le fichier `config.toml` de manière persistante.

## État
- **Status :** TERMINÉ ✓
- **Phase 1 :** COMPLÈTE ✓
