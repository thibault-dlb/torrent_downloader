import os
import sys
from pathlib import Path

if sys.platform == "win32":
    dll_path = Path(__file__).parent / "dlls"
    if dll_path.exists():
        os.add_dll_directory(str(dll_path))
