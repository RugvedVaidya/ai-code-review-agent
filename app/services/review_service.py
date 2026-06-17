from app.services.repo_loader import get_python_files
from app.analyzers.ruff_analyzer import run_ruff
from app.analyzers.bandit_analyzer import run_bandit
from app.reviewers.llm_reviewer import review_code


def analyze_repository(repo_path: str):
    results = []

    files = get_python_files(repo_path)

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()

        ruff_result = run_ruff(file)
        bandit_result = run_bandit(file)
        llm_review = review_code(code)

        results.append({
            "file": file,
            "ruff": ruff_result,
            "bandit": bandit_result,
            "review": llm_review
        })

    return results