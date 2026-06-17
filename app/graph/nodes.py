from app.services.repo_loader import get_python_files
from app.analyzers.ruff_analyzer import run_ruff
from app.analyzers.bandit_analyzer import run_bandit
from app.reviewers.llm_reviewer import review_code


def load_repository(state):
    files = get_python_files(state["repo_path"])

    return {
        **state,
        "files": files,
        "results": []
    }


def analyze_files(state):
    results = []

    for file in state["files"]:

        with open(file, "r", encoding="utf-8") as f:
            code = f.read()

        results.append({
            "file": file,
            "ruff": run_ruff(file),
            "bandit": run_bandit(file),
            "review": review_code(code)
        })

    return {
        **state,
        "results": results
    }