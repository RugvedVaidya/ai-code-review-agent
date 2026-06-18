from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

github_client = Github(
    os.getenv("GITHUB_TOKEN")
)

def parse_pr_url(pr_url):

    parts = pr_url.split("/")

    owner = parts[3]
    repo = parts[4]
    pr_number = int(parts[6])

    return owner, repo, pr_number

def get_pr_files(pr_url):

    owner, repo, pr_number = parse_pr_url(
        pr_url
    )

    repository = github_client.get_repo(
        f"{owner}/{repo}"
    )

    pull_request = repository.get_pull(
        pr_number
    )

    changed_files = []

    for file in pull_request.get_files():

        changed_files.append({
            "filename": file.filename,
            "patch": file.patch
        })

    return changed_files