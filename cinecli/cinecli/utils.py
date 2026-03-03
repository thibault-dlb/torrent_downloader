import winreg
import os
from pathlib import Path

def find_vlc_path() -> str:
    """
    Tente de trouver le chemin de VLC sur Windows.
    Retourne une chaîne vide si non trouvé.
    """
    # 1. Recherche via le registre Windows
    registry_paths = [
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\vlc.exe"),
        (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\vlc.exe"),
    ]

    for hkey, key_path in registry_paths:
        try:
            with winreg.OpenKey(hkey, key_path) as key:
                path, _ = winreg.QueryValueEx(key, "")
                if os.path.exists(path):
                    return path
        except (FileNotFoundError, OSError):
            continue

    # 2. Chemins d'installation standards
    standard_paths = [
        r"C:\Program Files\VideoLAN\VLC\vlc.exe",
        r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe",
    ]

    for path in standard_paths:
        if os.path.exists(path):
            return path

    return ""

def check_write_permission(path: str) -> bool:
    """
    Vérifie si on peut écrire dans le dossier spécifié.
    """
    p = Path(path)
    if not p.exists():
        try:
            p.mkdir(parents=True, exist_ok=True)
        except Exception:
            return False

    temp_file = p / ".cinecli_write_test"
    try:
        temp_file.touch()
        temp_file.unlink()
        return True
    except (PermissionError, OSError):
        return False
