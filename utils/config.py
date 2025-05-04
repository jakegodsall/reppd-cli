import yaml
from pathlib import Path

def get_config_path() -> str:
    """
    Get the path to the configuration file.
    """
    return Path.home() / ".reppd" / "config.yaml"

def create_config_file(default_data: dict = None) -> str:
    """
    Create the config file in the ~/.reppd/ directory
    if not already exists. Returns the path to the file.
    """
    config_path = get_config_path()
    config_dir = config_path.parent

    # Create the directory if it doesn't exist
    config_dir.mkdir(parents=True, exist_ok=True)

    # Create the file if it doesn't exist
    if not config_path.exists():
        default_data = default_data or {"token": ""}
        config_path.write_text(yaml.dump(default_data))

    return config_path

def get_config_data() -> dict:
    """
    Loads YAML config data, or creates a default config if missing.
    """
    create_config_file()
    config_path = get_config_path()
    try:
        return yaml.safe_load(config_path.read_text()) or {}
    except Exception as e:
        raise RuntimeError(f"Failed to load config file: {e}")