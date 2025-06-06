"""This is an automatically generated file. Do not modify it.

This file was generated using `langgraph-gen` version .
To regenerate this file, run `langgraph-gen` with the source `yaml` file as an argument.

Usage:

1. Add the generated file to your project.
2. Create a new agent using the stub.

Below is a sample implementation of the generated stub:

```python
from typing_extensions import TypedDict

from stub import test_langgraph_trigger

class SomeState(TypedDict):
    # define your attributes here
    foo: str

# Define stand-alone functions
def first_node(state: SomeState) -> dict:
    print("In node: first_node")
    return {
        # Add your state update logic here
    }


def second_node(state: SomeState) -> dict:
    print("In node: second_node")
    return {
        # Add your state update logic here
    }


def decision_node(state: SomeState) -> dict:
    print("In node: decision_node")
    return {
        # Add your state update logic here
    }


def routing_function(state: SomeState) -> str:
    print("In condition: routing_function")
    raise NotImplementedError("Implement me.")


agent = test_langgraph_trigger(
    state_schema=SomeState,
    impl=[
        ("first_node", first_node),
        ("second_node", second_node),
        ("decision_node", decision_node),
        ("routing_function", routing_function),
    ]
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
"""

from typing import Callable, Any, Optional, Type

from langgraph.constants import START, END  # noqa: F401
from langgraph.graph import StateGraph


def test_langgraph_trigger(
    *,
    state_schema: Optional[Type[Any]] = None,
    config_schema: Optional[Type[Any]] = None,
    input: Optional[Type[Any]] = None,
    output: Optional[Type[Any]] = None,
    impl: list[tuple[str, Callable]],
) -> StateGraph:
    """Create the state graph for test_langgraph_trigger."""
    # Declare the state graph
    builder = StateGraph(
        state_schema, config_schema=config_schema, input=input, output=output
    )

    nodes_by_name = {name: imp for name, imp in impl}

    all_names = set(nodes_by_name)

    expected_implementations = {
        "first_node",
        "second_node",
        "decision_node",
        "routing_function",
    }

    missing_nodes = expected_implementations - all_names
    if missing_nodes:
        raise ValueError(f"Missing implementations for: {missing_nodes}")

    extra_nodes = all_names - expected_implementations

    if extra_nodes:
        raise ValueError(
            f"Extra implementations for: {extra_nodes}. Please regenerate the stub."
        )

    # Add nodes
    builder.add_node("first_node", nodes_by_name["first_node"])
    builder.add_node("second_node", nodes_by_name["second_node"])
    builder.add_node("decision_node", nodes_by_name["decision_node"])

    # Add edges
    builder.add_edge("first_node", "second_node")
    builder.add_edge("second_node", "decision_node")
    builder.add_conditional_edges(
        "decision_node",
        nodes_by_name["routing_function"],
        {
            "path_a": "path_a_node",
            "path_b": "path_b_node",
        }
    )
    return builder
