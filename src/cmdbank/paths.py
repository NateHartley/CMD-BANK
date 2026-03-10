from platformdirs import user_data_dir, user_cache_dir, user_config_dir
from pathlib import Path

APP_NAME = "cmdbank"
DATA_DIR = Path(user_data_dir(APP_NAME)) / "Data"   # macOS '/Users/<USERNAME>/Library/Application Support/cmdbank/Data'
CACHE_DIR = Path(user_cache_dir(APP_NAME))          # macOS '/Users/<USERNAME>/Library/Caches/cmdbank'
READCMD = CACHE_DIR / ".READCMD"                    # macOS '/Users/<USERNAME>/Library/Caches/cmdbank/.READCMD'
CONFIG_DIR = Path(user_config_dir(APP_NAME))        # macOS '/Users/<USERNAME>/Library/Application Support/cmdbank'
CONFIG = CONFIG_DIR / "config.toml"                 # macOS '/Users/<USERNAME>/Library/Application Support/cmdbank/config.toml'

PLACEHOLDER_CONFIG_DATA = """
(Placeholder config file for cmdbank)
"""

def init_paths():
    for path in (DATA_DIR, CACHE_DIR, CONFIG_DIR):
        path.mkdir(parents=True, exist_ok=True)

    if not READCMD.exists():
        READCMD.touch()

    if not CONFIG.exists():
        CONFIG.write_text(PLACEHOLDER_CONFIG_DATA)
