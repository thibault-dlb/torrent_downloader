from pathlib import Path
import tomllib
import tomli_w
import os
from cinecli.utils import find_vlc_path

CONFIG_DIR = Path.home() / ".config" / "cinecli"
CONFIG_PATH = CONFIG_DIR / "config.toml"

DEFAULT_CONFIG = {
    "temp_path": str(Path(os.environ.get("TEMP", ".")) / "cinecli-cache"),
    "permanent_path": "",
    "vlc_path": find_vlc_path(),
    "default_action": "magnet",
}

def load_config():
    if not CONFIG_PATH.exists():
        return DEFAULT_CONFIG
    
    with open(CONFIG_PATH, "rb") as f:
        config = tomllib.load(f)
    
    # Fusionner avec les défauts pour garantir la présence des clés
    return {**DEFAULT_CONFIG, **config}

def save_config(config):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "wb") as f:
        tomli_w.dump(config, f)
