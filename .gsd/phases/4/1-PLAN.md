---
phase: 4
plan: 1
wave: 1
---

# Plan 4.1: Nettoyage du Code et Finalisation

## Objectif
S'assurer que le code est propre, que tous les imports inutilisés sont supprimés, et que la documentation reflète l'état final du projet selon SPEC.md.

## Context
- .gsd/SPEC.md
- Toutes les implémentations de la Phase 1 à 3.
- `cinecli/cinecli/cli.py`
- `cinecli/cinecli/downloader.py`
- `cinecli/cinecli/ui.py`
- `cinecli/cinecli/utils.py`

## Tasks

<task type="auto">
  <name>Nettoyage des imports et variables inutilisées</name>
  <files>cinecli/cinecli/*.py</files>
  <action>
    - Inspecter `cli.py` pour retirer l'ancienne logique de `magnets.py` (ouverture via client externe) qui n'est plus proposée puisqu'on utilise le mode interne 1, 2 ou 3.
    - Supprimer `magnets.py` si son utilité a totalement disparu, ou l'intégrer aux utilitaires. (Note: `build_magnet` est encore utilisé, mais `open_magnet` ou `download_torrent` via Transmission non).
    - Vérifier les `import` non utilisés dans tous les fichiers `cinecli`.
  </action>
  <verify>Exécution de `python -m py_compile` sur tous les fichiers pour garantir l'absence d'erreurs de syntaxe, et validation visuelle du code.</verify>
  <done>Le code est propre, sans dépendances orphelines.</done>
</task>

<task type="auto">
  <name>Mise à jour du README et de l'aide CLI</name>
  <files>cinecli/README.md, cinecli/cinecli/cli.py</files>
  <action>
    - Mettre à jour les "help" strings dans `typer.Typer()` pour refléter les nouvelles capacités de téléchargement séquentiel et de buffer.
    - Préparer un paragraphe pour l'utilisateur résumant comment utiliser le mode interactif ou le nouveau flux `watch`.
  </action>
  <verify>`python -m cinecli --help` affiche la documentation mise à jour.</verify>
  <done>La documentation interne et CLI est à jour avec la v0.2.0.</done>
</task>

## Success Criteria
- [ ] L'application ne contient plus de code mort concernant Transmission ou le téléchargement via navigateur, puisque tout est interne maintenant.
- [ ] La CLI est claire et documentée.
- [ ] Tous les critères de la SPEC.md sont officiellement cochés.
