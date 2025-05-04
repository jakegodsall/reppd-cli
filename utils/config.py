import yaml
from pathlib import Path

def get_config_path() -> str:
    """
    Get the path to the configuration file.
    """
    return Path.home() / ".reppd" / "config.yaml"

def create_config_file(default_data: dict = None) -> str:
    """
    Create or overwrite the config file in the ~/.reppd/ directory.
    Returns the path to the file.
    """
    config_path = get_config_path()
    config_dir = config_path.parent

    # Create the directory if it doesn't exist
    config_dir.mkdir(parents=True, exist_ok=True)

    # Set default config if not provided
    default_data = default_data or None

    # Always write/overwrite the config file
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
    
def configure_flow():
    """
    The full flow for configuring the application.
    """
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    config_path = create_config_file({
        "email": email,
        "password": password
    })