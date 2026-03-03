import time
import libtorrent as lt
from pathlib import Path

class TorrentDownloader:
    def __init__(self, save_path: str):
        self.save_path = Path(save_path)
        self.ses = lt.session({
            'listen_interfaces': '0.0.0.0:6881',
            'alert_mask': lt.alert.category_t.status_notification
        })
        self.ses.add_dht_router("router.bittorrent.com", 6881)
        self.ses.add_dht_router("router.utorrent.com", 6881)
        self.ses.add_dht_router("dht.transmissionbt.com", 6881)
        self.handle = None

    def add_magnet(self, magnet_link: str, sequential: bool = True):
        params = lt.parse_magnet_uri(magnet_link)
        params.save_path = str(self.save_path)
        self.handle = self.ses.add_torrent(params)
        
        if sequential:
            self.handle.set_sequential_download(True)
        
        return self.handle

    def wait_for_metadata(self, timeout: int = 30):
        """Attend que les métadonnées du torrent soient récupérées."""
        start_time = time.time()
        while not self.handle.has_metadata():
            if time.time() - start_time > timeout:
                return False
            time.sleep(1)
        return True

    def get_main_file(self):
        """Identifie le plus gros fichier (probablement le film)."""
        if not self.handle or not self.handle.has_metadata():
            return None
        
        info = self.handle.get_torrent_info()
        best_file_index = -1
        max_size = 0
        
        for i in range(info.num_files()):
            if info.files().file_size(i) > max_size:
                max_size = info.files().file_size(i)
                best_file_index = i
        
        return {
            "index": best_file_index,
            "path": info.files().file_path(best_file_index),
            "size": max_size
        }

    def prioritize_streaming_pieces(self):
        """Met la priorité max sur les 5% du début et 1% de la fin des pièces."""
        if not self.handle or not self.handle.has_metadata():
            return
            
        info = self.handle.get_torrent_info()
        num_pieces = info.num_pieces()
        
        # 5% du début (au moins 5 pièces)
        start_pieces = max(5, int(num_pieces * 0.05))
        # 1% de la fin (au moins 2 pièces)
        end_pieces = max(2, int(num_pieces * 0.01))
        
        for i in range(min(start_pieces, num_pieces)):
            self.handle.piece_priority(i, 7)
            
        for i in range(max(0, num_pieces - end_pieces), num_pieces):
            self.handle.piece_priority(i, 7)

    def get_status(self):
        if not self.handle:
            return None
        return self.handle.status()

    def is_finished(self):
        if not self.handle:
            return False
        return self.handle.is_finished()
