from pathlib import Path


def get_root_path() -> Path:
    current_path = Path.cwd()
    while not (current_path / 'pyproject.toml').is_file():
        current_path = current_path.parent
    return current_path
