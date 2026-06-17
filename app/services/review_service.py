from app.graph.workflow import build_graph

# Build graph once when application starts
graph = build_graph()


def analyze_repository(repo_url=None, repo_path=""):
    """
    Analyze either:
    - A local repository (repo_path)
    - A GitHub repository (repo_url)
    """

    state = {
        # Input
        "repo_url": repo_url,
        "repo_path": repo_path,

        # Repository information
        "files": [],

        # Analysis outputs
        "ruff_results": [],
        "bandit_results": [],
        "review_results": [],

        # Test generation & execution
        "generated_tests": [],
        "test_results": [],

        # Reflection loop
        "reflection_feedback": [],
        "retry_count": 0,
        "max_retries": 3,

        # Final output
        "results": [],
        "report_path": ""
    }

    result = graph.invoke(state)

    return {
        "report_path": result.get("report_path", ""),
        "results": result.get("results", []),
        "retry_count": result.get("retry_count", 0)
    }