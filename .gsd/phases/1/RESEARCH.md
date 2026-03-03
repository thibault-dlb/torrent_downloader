# Research Phase 1: Configuration & VLC Detection (Windows)

## VLC Detection on Windows

### Standard Installation Paths
1. `C:\Program Files\VideoLAN\VLC\vlc.exe`
2. `C:\Program Files (x86)\VideoLAN\VLC\vlc.exe`

### Registry Keys
- **Primary**: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\vlc.exe`
  - The default value is the path to `vlc.exe`.
- **Secondary**: `HKEY_LOCAL_MACHINE\SOFTWARE\VideoLAN\VLC`
  - Value `InstallDir` contains the directory.

### Python Implementation
Using `winreg` (standard library) to query the registry.
```python
import winreg
try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\vlc.exe") as key:
        vlc_path = winreg.QueryValue(key, None)
except FileNotFoundError:
    # Fallback to file search or secondary keys
    pass
```

## Libtorrent Availability
`libtorrent` is available on PyPI as `python-libtorrent` (legacy) or `libtorrent`. 
Recommended: `pip install libtorrent`.
Verification: `import libtorrent as lt; print(lt.version)`

## Permission Validation
Using `os.access(path, os.W_OK)` is often insufficient on Windows for network drives or specific ACLs.
Better approach: Attempt to create a small temporary file and delete it.
