import sys
import os
from pathlib import Path

# Ajouter le dossier cinecli au path
sys.path.append(str(Path.cwd() / "cinecli"))

from cinecli.config import load_config
from cinecli.downloader import TorrentDownloader

# Magnet de test (Debian)
MAGNET = "magnet:?xt=urn:btih:d1ba87455d3780512f451433f5d5225c52f63884&dn=debian-12.9.0-amd64-netinst.iso"

def test_downloader():
    print("--- Test Libtorrent Downloader ---")
    
    config = load_config()
    temp_path = config.get("temp_path", "./test-cache")
    
    # Créer le dossier s'il n'existe pas
    os.makedirs(temp_path, exist_ok=True)
    
    print(f"Utilisation du dossier temporaire: {temp_path}")
    
    downloader = TorrentDownloader(temp_path)
    handle = downloader.add_magnet(MAGNET)
    
    print("Récupération des métadonnées (max 30s)...")
    if downloader.wait_for_metadata(30):
        print("✅ Métadonnées récupérées !")
        main_file = downloader.get_main_file()
        print(f"Fichier principal détecté: {main_file['path']} ({main_file['size'] / 1024 / 1024:.2f} MB)")
        
        status = downloader.get_status()
        print(f"Statut actuel: {status.state}")
        print(f"Progression: {status.progress * 100:.1f}%")
        
    else:
        print("❌ Échec de la récupération des métadonnées (vérifiez votre connexion)")

if __name__ == "__main__":
    test_downloader()
