from typing import TypedDict, List


class ReviewState(TypedDict):
    repo_path: str
    files: List[str]
    results: List[dict]