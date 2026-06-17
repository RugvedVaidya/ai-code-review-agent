from git import repo 
from pathlib import Path
import shutil

def clone_repository(repo_url):

    repos_dir = Path("repositories")

    repos_dir.mkdir(
        exist_ok=True
    )

    repo_name = (
        repo_url.split("/")
        [-1]
        .replace(".git", "")
    )

    repo_path = (
        repos_dir / repo_name
    )

    if repo_path.exists():
        shutil.rmtree(repo_path)

    Repo.clone_from(
        repo_url,
        repo_path
    )

    return str(repo_path)