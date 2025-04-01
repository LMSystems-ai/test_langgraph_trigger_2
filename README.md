# test_langgraph_trigger



## Overview


### Nodes

- **first_node**: No description provided.
- **second_node**: No description provided.
- **decision_node**: No description provided.

### Edge Flow

- **first_node** → **second_node**- **second_node** → **decision_node**- **decision_node** conditionally routes to **path_a**, **path_b** based on **routing_function**
## Getting Started

1. Install the required dependencies:
   ```bash
   pip install -e .
   ```

2. Run the agent:
   ```bash
   langgraph dev
   ```

## Project Structure

- `lmsys_impl.py`: Main implementation file
- `nodes/state.py`: State definition
- `nodes/`: Individual node implementations
- `langgraph.json`: LangGraph configuration