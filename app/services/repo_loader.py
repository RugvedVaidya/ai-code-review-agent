from pathlib import Path


def get_python_files(repo_path: str):
    path = Path(repo_path)

    return [
        str(file)
        for file in path.rglob("*.py")
        if ".venv" not in str(file)
    ]