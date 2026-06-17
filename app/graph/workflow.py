from langgraph.graph import StateGraph, END

from app.graph.state import ReviewState
from app.graph.nodes import (
    load_repository,
    analyze_files
)


def build_graph():

    graph = StateGraph(ReviewState)

    graph.add_node(
        "load_repository",
        load_repository
    )

    graph.add_node(
        "analyze_files",
        analyze_files
    )

    graph.set_entry_point(
        "load_repository"
    )

    graph.add_edge(
        "load_repository",
        "analyze_files"
    )

    graph.add_edge(
        "analyze_files",
        END
    )

    return graph.compile()