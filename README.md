# Torrent Downloader & Streamer

A major fork and extension of **[CineCLI](https://github.com/eyeblech/cinecli)** featuring an integrated real bittorrent engine (`libtorrent`) and an intelligent streaming system coupled with **VLC**.

## Overview
This project aims to transform CineCLI, initially a simple catalog and "magnet passer" (limiting the user to external clients), into an **"all-in-one"** solution:
* Search for your movies from the command line.
* Watch them instantly via **streaming**. Downloading happens in the background, and the video starts playing directly on VLC through a secure "Pre-buffering" system.
* Automatic cache cleaning upon closing.

---

## 🚀 Major New Features (v0.2.0)

Compared to the original repository, this manager includes:
- **Integrated BitTorrent Engine**: No more complex dependencies; the project directly downloads torrent pieces using the C++ `libtorrent` library compiled for Python.
- **Automatic Pre-Buffering**: VLC only launches once the beginning and end MP4/MKV headers are downloaded or after a sufficient buffer (2%), ensuring no crashes occur.
- **Mode Selection**:
    - `Watch` Mode (Disposable Temporary Cache)
    - `Download` Mode (Permanent Storage)
    - `Hybrid` Mode (Download permanently while watching)
- **Robust Cache Cleaning**: A Windows file locking bypass has been implemented to ensure safe and reliable cleaning.
- **Terminal UI**: `Rich` progress bars displaying remaining time, transfer speeds, and detection of manual video player closure.

## 🛠️ Installation & Prerequisites

1. **Python 3.12** is recommended (for compatibility with Windows `libtorrent` DLLs).
2. Clone this repository.

```powershell
# Navigate to the subfolder containing the project
cd cinecli

# Install the package for your user account
pip install -e .
```

*Windows Note*: If the `cinecli` command is not recognized after installation, make sure `C:\Users\<YourName>\AppData\Roaming\Python\Python312\Scripts` is added to your environment variables (`PATH`).

## 🎬 Usage

* **Search and choose a movie interactively (Highly recommended):**
  ```powershell
  cinecli interactive
  ```
  The assistant will ask you to search for a title, choose a quality, and select your action (Watch or Download).

* **Quick search:**
  ```powershell
  cinecli search "Batman"
  ```
* **Launch a movie by its ID:**
  ```powershell
  cinecli watch 1234
  ```

* **Configuration:**
  ```powershell
  cinecli config --path "D:\Movies" --vlc "C:\Program Files\VideoLAN\VLC\vlc.exe"
  ```

## 🙏 Credits and Acknowledgments

The entire YTS search system, the Terminal UI mechanics (`Rich`), and the overall CLI structure (`Typer`) were originally developed by **[eyeblech](https://github.com/eyeblech)** in his [CineCLI](https://github.com/eyeblech/cinecli) repository.
This project builds on top of it by adding an active Peer-to-Peer network engine.

---
**Developed and carefully extended via the GSD Methodology.**
