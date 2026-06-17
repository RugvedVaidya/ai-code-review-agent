from langgraph.graph import StateGraph, END

from app.graph.state import ReviewState

from app.graph.nodes import (
    load_repository,
    ruff_agent,
    security_agent,
    review_agent,
    aggregate_results
)
def build_graph():

    graph = StateGraph(
        ReviewState
    )

    graph.add_node(
        "load_repository",
        load_repository
    )

    graph.add_node(
        "ruff_agent",
        ruff_agent
    )

    graph.add_node(
        "security_agent",
        security_agent
    )

    graph.add_node(
        "review_agent",
        review_agent
    )

    graph.add_node(
        "aggregate_results",
        aggregate_results
    )

    graph.set_entry_point(
        "load_repository"
    )

    graph.add_edge(
        "load_repository",
        "ruff_agent"
    )

    graph.add_edge(
        "ruff_agent",
        "security_agent"
    )

    graph.add_edge(
        "security_agent",
        "review_agent"
    )

    graph.add_edge(
        "review_agent",
        "aggregate_results"
    )

    graph.add_edge(
        "aggregate_results"
    )

    graph.add_node(
        "test_generation_agent",
        test_generation_agent
    )

    graph.add_node(
        "save_tests_agent",
        save_tests_agent
    )

    graph.add_node(
        "pytest_agent",
        pytest_agent
    )
    
    graph.add_conditional_edges(
        "pytest_agent",
        route_after_tests,
        {
            "passed": "aggregate_results",
            "failed": "reflection_agent",
            "max_retries": "aggregate_results"
        }
    )
    
    graph.add_node(
        "reflection_agent",
        reflection_agent
    )

    graph.add_node(
        "code_fix_agent",
        code_fix_agent
    )
    
    graph.add_edge(
        "reflection_agent",
        "code_fix_agent"
    )

    graph.add_edge(
        "code_fix_agent",
        "pytest_agent"
    )

    graph.add_node(
        "github_loader_agent",
        github_loader_agent
    )
    
    graph.set_entry_point(
        "github_loader_agent"
    )
    
    graph.add_edge(
        "github_loader_agent",
        "load_repository"
    )
    
    graph.add_node(
        "report_agent",
        report_agent
    )
    
    graph.add_edge(
        "aggregate_results",
        "report_agent"
    )
    
    graph.add_edge(
        "report_agent",
        END
    )
    return graph.compile()