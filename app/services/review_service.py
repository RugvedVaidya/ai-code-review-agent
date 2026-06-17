from app.graph.workflow import build_graph

graph = build_graph()


def analyze_repository(repo_path):

    state = {
        "repo_path": repo_path,
        "files": [],
        "ruff_results": [],
        "bandit_results": [],
        "review_results": [],
        "results": []
    }

    result = graph.invoke(state)

    return result["results"]