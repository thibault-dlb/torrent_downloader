---
phase: 1
plan: 1
wave: 1
---

# Plan 1.1: Refonte de la Configuration & Détection VLC

## Objectif
Mettre à jour le système de configuration pour supporter les chemins de téléchargement (permanent et temporaire) et implémenter la détection automatique de VLC sur Windows.

## Context
- .gsd/SPEC.md
- .gsd/DECISIONS.md
- .gsd/phases/1/RESEARCH.md
- cinecli/cinecli/config.py

## Tasks

<task type="auto">
  <name>Mise à jour de config.py</name>
  <files>cinecli/cinecli/config.py</files>
  <action>
    - Ajouter des valeurs par défaut pour `temp_path` (ex: %TEMP%/cinecli-cache).
    - Ajouter une fonction `save_config(config)` pour persister les changements.
    - S'assurer que les chemins sont gérés avec `pathlib.Path`.
  </action>
  <verify>python -c "from cinecli.config import load_config; print(load_config())"</verify>
  <done>La configuration peut charger et sauvegarder de nouveaux champs.</done>
</task>

<task type="auto">
  <name>Utilitaire de détection VLC</name>
  <files>cinecli/cinecli/utils.py</files>
  <action>
    - Créer `utils.py` s'il n'existe pas.
    - Implémenter `find_vlc_path()` en utilisant `winreg` et les chemins standards (voir RESEARCH.md).
    - Ajouter une fonction `check_write_permission(path)` qui tente de créer un fichier temporaire pour valider l'accès.
  </action>
  <verify>python -c "from cinecli.utils import find_vlc_path; print(f'VLC found at: {find_vlc_path()}')"</verify>
  <done>VLC est détecté automatiquement sur un système Windows standard.</done>
</task>

## Success Criteria
- [ ] Le fichier `config.toml` peut stocker `permanent_path` et `vlc_path`.
- [ ] VLC est localisé sans intervention utilisateur dans 90% des cas.
