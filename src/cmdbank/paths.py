from platformdirs import user_data_dir, user_cache_dir, user_config_dir
from pathlib import Path

APP_NAME = "cmdbank"
DATA_DIR = Path(user_data_dir(APP_NAME)) / "Data"
CACHE_DIR = Path(user_cache_dir(APP_NAME))
READCMD = CACHE_DIR / ".READCMD"
CONFIG_DIR = Path(user_config_dir(APP_NAME))
CONFIG = CONFIG_DIR / "config.toml"

DEFAULT_CONFIG_DATA = """
copy_command_to_clipboard = false
sort_files_alphabetically = true
"""

def init_paths():
    for path in (DATA_DIR, CACHE_DIR, CONFIG_DIR):
        path.mkdir(parents=True, exist_ok=True)

    if not READCMD.exists():
        READCMD.touch()

    if not CONFIG.exists():
        CONFIG.write_text(DEFAULT_CONFIG_DATA)
