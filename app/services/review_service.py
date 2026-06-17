from app.graph.workflow import build_graph

graph = build_graph()


def analyze_repository(repo_path):

    state = {
        "repo_path": repo_path,
        "files": [],
        "ruff_results": [],
        "bandit_results": [],
        "review_results": [],
        "generated_tests": [],
        "test_results": [],
        "reflection_feedback": [],
        "retry_count": 0,
        "max_retries": 3,
        "results": []
    }

    result = graph.invoke(state)

    return result["results"]