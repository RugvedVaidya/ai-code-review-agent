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
        "aggregate_results",
        END
    )

    return graph.compile()