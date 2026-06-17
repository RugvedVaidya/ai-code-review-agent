from app.graph.workflow import build_graph

graph = build_graph()


def analyze_repository(repo_path: str):

    result = graph.invoke({
        "repo_path": repo_path,
        "files": [],
        "results": []
    })

    return result["results"]