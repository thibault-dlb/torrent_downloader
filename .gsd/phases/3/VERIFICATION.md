# Phase 3 Verification: Intégration avancée de VLC et Streaming

## Must-Haves
- [x] Priorisation de téléchargement pour MP4/MKV (Les atomes existent au début/fin) — VERIFIED (`prioritize_streaming_pieces` défini au lancement du torrent)
- [x] Pre-buffering du torrent — VERIFIED (15 secondes max ou 2% atteints avant lancement VLC)
- [x] Surveillance temps-réel de VLC — VERIFIED (Dans `ui.py`, la boucle `manage_download_progress` interrompt `libtorrent` si `vlc_process` crashe ou est fermé manuellement).
- [x] Résilience au verrou Windows — VERIFIED (Boucle retry avec `time.sleep` implémentée)

## Verdict: PASS

VLC est désormais capable d'ouvrir la vidéo en mode streaming brut avec `libtorrent` sans interruption prématurée, et avec une gestion propre du cycle de vie sous Windows.
