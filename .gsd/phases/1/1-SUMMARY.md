# Plan 1.1 Summary: Refonte de la Configuration & Détection VLC

## Ce qui a été fait
- Mise à jour de `cinecli/config.py` :
    - Ajout de `DEFAULT_CONFIG` avec `temp_path`, `permanent_path`, `vlc_path` et `default_action`.
    - Implémentation de `save_config(config)` pour persister les paramètres.
    - Ajout de la dépendance `tomli-w` dans `pyproject.toml` (et installation locale).
- Création de `cinecli/utils.py` :
    - Fonction `find_vlc_path()` : Recherche VLC via le registre Windows (`SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\vlc.exe`) et les dossiers standards de `Program Files`.
    - Fonction `check_write_permission(path)` : Validation des permissions d'écriture par création/suppression d'un fichier temporaire.

## Vérification
- `find_vlc_path()` a retourné `C:\Program Files\VideoLAN\VLC\vlc.exe`.
- `load_config()` retourne bien les valeurs par défaut incluant le chemin de VLC détecté.

## État
- **Status :** TERMINÉ ✓
- **Suivant :** Plan 1.2 (Commandes CLI)
