# Torrent Downloader & Streamer

Un fork et une extension majeure de **[CineCLI](https://github.com/eyeblech/cinecli)** intégrant un véritable moteur torrent interne (`libtorrent`) et un système de streaming intelligent couplé à **VLC**.

## Présentation
Ce projet a pour but de transformer CineCLI, initialement un simple catalogueur et "passeur de magnet" (limitant l'utilisateur à des clients externes), en une solution **"tout-en-un"** :
* Cherchez vos films en ligne de commande.
* Regardez-les instantanément en **streaming**. Le téléchargement se fait en fond, la vidéo se lance sans attendre sur VLC via un système de "Pre-buffering" sécurisé.
* Nettoyage automatique des caches à la fermeture.

---

## 🚀 Nouvelles Fonctionnalités Majeures (v0.2.0)

Par rapport au dépôt d'origine, ce gestionnaire inclut :
- **Moteur BitTorrent Intégré** : Fini les dépendances complexes, le projet télécharge directement les pièces des torrents grâce à la bibliothèque C++ `libtorrent` compilée pour Python.
- **Pre-Buffering Automatique** : VLC ne se lance qu'une fois que les entêtes MP4/MKV de début et de fin sont téléchargés ou après un tampon suffisant (2%), garantissant l'absence de crash.
- **Sélection des Modes** :
    - Mode `Watch` (Cache Temporaire jetable)
    - Mode `Download` (Enregistrement Permanent)
    - Mode `Hybrid` (Télécharger définitivement tout en regardant)
- **Nettoyage Robuste de Cache** : Un contournement des verrous fichiers de Windows (`Locking`) a été mis en place pour garantir un nettoyage sûr.
- **UI Terminal** : Barres de progression `Rich` avec temps restant, vitesses de transfert, et détection de la fermeture manuelle du lecteur vidéo.

## 🛠️ Installation & Prérequis

1. **Python 3.12** est recommandé (pour la compatibilité des DLLs Windows de _libtorrent_).
2. Cloner ce dépôt.

```powershell
# Déplacez-vous dans le sous-dossier contenant le projet
cd cinecli

# Installez le package pour votre compte utilisateur
pip install -e .
```

*Note Windows* : Si la commande `cinecli` n'est pas reconnue après l'installation, assurez-vous que `C:\Users\<VotreNom>\AppData\Roaming\Python\Python312\Scripts` est ajouté dans vos variables d'environnement (`PATH`).

## 🎬 Utilisation

* **Chercher et choisir un film de manière interactive (Le plus recommandé) :**
  ```powershell
  cinecli interactive
  ```
  L'assistant vous demandera de chercher un titre, choisir une qualité, et sélectionner votre action (Regarder ou Télécharger).

* **Recherche rapide :**
  ```powershell
  cinecli search "Batman"
  ```
* **Lancer un film par son ID :**
  ```powershell
  cinecli watch 1234
  ```

* **Configuration :**
  ```powershell
  cinecli config --path "D:\Films" --vlc "C:\Program Files\VideoLAN\VLC\vlc.exe"
  ```

## 🙏 Crédits et Remerciements

Tout le système de recherche via YTS, la mécanique de l'UI Terminal (`Rich`), et la structure CLI globale (`Typer`) ont été développés originellement par **[eyeblech](https://github.com/eyeblech)** sur son dépôt [CineCLI](https://github.com/eyeblech/cinecli). 
Ce projet ajoute par-dessus la mécanique de réseau Pair-à-Pair active.

---
**Développé et étendu avec soin via la GSD Methodology.**
