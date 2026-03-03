---
phase: 1
plan: 2
wave: 1
---

# Plan 1.2: Commandes CLI & Initialisation

## Objectif
Ajouter les commandes nécessaires pour configurer le projet via la ligne de commande et gérer la première initialisation du dossier de téléchargement.

## Context
- .gsd/SPEC.md
- .gsd/DECISIONS.md
- cinecli/cinecli/cli.py
- cinecli/cinecli/config.py
- cinecli/cinecli/utils.py

## Tasks

<task type="auto">
  <name>Ajout de la commande 'config'</name>
  <files>cinecli/cinecli/cli.py</files>
  <action>
    - Ajouter une commande `config` à l'application typer.
    - Options : `--path` (pour le dossier permanent) et `--vlc` (pour forcer le chemin VLC).
    - Valider les chemins fournis via `check_write_permission`.
  </action>
  <verify>python -m cinecli.cli config --path "."</verify>
  <done>L'utilisateur peut modifier sa configuration via la CLI.</done>
</task>

<task type="auto">
  <name>Logique de premier lancement</name>
  <files>cinecli/cinecli/cli.py</files>
  <action>
    - Dans la fonction main ou via un callback, vérifier si `permanent_path` est défini.
    - Si absent, demander interactivement à l'utilisateur de choisir un dossier.
    - S'assurer que VLC est aussi configuré (automatiquement ou manuellement).
  </action>
  <verify>python -m cinecli.cli --help</verify>
  <done>Le programme demande la configuration manquante au démarrage.</done>
</task>

## Success Criteria
- [ ] La commande `cinecli config --path X` met à jour le fichier de config.
- [ ] Un premier lancement sans config déclenche le mode interactif.
