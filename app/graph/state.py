from typing import TypedDict, List


class ReviewState(TypedDict):

    repo_path: str

    files: List[str]

    ruff_results: List[dict]
    bandit_results: List[dict]
    review_results: List[dict]

    generated_tests: List[dict]

    test_results: List[dict]

    results: List[dict]