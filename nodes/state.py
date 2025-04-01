"""
State definition for test_langgraph_trigger
"""

from typing import Dict, Any, TypedDict


class State(TypedDict):
    """State for the test_langgraph_trigger workflow."""
    # Define your state fields here
    input: str
    output: Any