# Plan 2.1 Summary: Intégration Libtorrent & Logique Séquentielle

## Ce qui a été fait
- Installation et configuration de `libtorrent` (v2.0.11) sur Python 3.12.
- Ajout manuel des DLL OpenSSL 1.1.1 manquantes pour corriger l'erreur d'importation sous Windows.
- Création de `cinecli/downloader.py` :
    - Classe `TorrentDownloader` avec session DHT pour les métadonnées.
    - Activation du mode `set_sequential_download(True)`.
    - Méthode pour trouver le fichier vidéo principal (`get_main_file()`).
- Mise à jour de `cinecli/magnets.py` pour supporter le mode de téléchargement interne.

## Vérification
- `libtorrent` est importable et sa version est reconnue (2.0.11).
- La session peut analyser des liens magnets et activer le mode séquentiel manuellement.

## État
- **Status :** TERMINÉ ✓
- **Suivant :** Plan 2.2 (Progression UI)
