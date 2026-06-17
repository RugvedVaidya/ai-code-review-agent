from app.services.repo_loader import get_python_files
from app.analyzers.ruff_analyzer import run_ruff
from app.analyzers.bandit_analyzer import run_bandit
from app.reviewers.llm_reviewer import review_code
from app.generators.test_generator import (
    generate_tests
)
from pathlib import Path
from app.executors.pytest_executor import (
    run_pytest
)

def load_repository(state):

    files = get_python_files(
        state["repo_path"]
    )

    return {
        **state,
        "files": files
    }

def ruff_agent(state):

    ruff_results = []

    for file in state["files"]:

        result = run_ruff(file)

        ruff_results.append({
            "file": file,
            "ruff": result
        })

    return {
        **state,
        "ruff_results": ruff_results
    }
    
def security_agent(state):

    bandit_results = []

    for file in state["files"]:

        result = run_bandit(file)

        bandit_results.append({
            "file": file,
            "bandit": result
        })

    return {
        **state,
        "bandit_results": bandit_results
    }
    
def review_agent(state):

    review_results = []

    for file in state["files"]:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            code = f.read()

        review = review_code(code)

        review_results.append({
            "file": file,
            "review": review
        })

    return {
        **state,
        "review_results": review_results
    }
    
def aggregate_results(state):

    final_results = []

    for file in state["files"]:

        ruff = next(
            x["ruff"]
            for x in state["ruff_results"]
            if x["file"] == file
        )

        bandit = next(
            x["bandit"]
            for x in state["bandit_results"]
            if x["file"] == file
        )

        review = next(
            x["review"]
            for x in state["review_results"]
            if x["file"] == file
        )

        final_results.append({
            "file": file,
            "ruff": ruff,
            "bandit": bandit,
            "review": review
        })

    return {
        **state,
        "results": final_results
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
    
def test_generation_agent(state):

    generated_tests = []

    for file in state["files"]:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            code = f.read()

        tests = generate_tests(code)

        generated_tests.append({
            "file": file,
            "tests": tests
        })

    return {
        **state,
        "generated_tests": generated_tests
    }
    
def save_tests_agent(state):

    for item in state["generated_tests"]:

        source_file = Path(item["file"])

        test_path = (
            source_file.parent
            /
            f"test_{source_file.name}"
        )

        with open(
            test_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(item["tests"])

    return state

def pytest_agent(state):

    test_results = []

    for item in state["generated_tests"]:

        source_file = Path(item["file"])

        test_path = (
            source_file.parent
            /
            f"test_{source_file.name}"
        )

        result = run_pytest(
            str(test_path)
        )

        test_results.append({
            "file": item["file"],
            "result": result
        })

    return {
        **state,
        "test_results": test_results
    }
    
def tests_passed(state):

    for item in state["test_results"]:

        if not item["result"]["success"]:
            return "failed"

    return "passed"