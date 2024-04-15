# FamilyAI Project Structure Update

## General Data Handling Note

- **Markdown Files Handling**: Agents monitor and interact with `.md` files across the entire `C:\SymbieFamily\` directory structure, enabling dynamic interactions and task allocations.

## Directory: `FamilyCrewAI/agents`

### Files and Descriptions

#### `base_member.py`

- **Current State**: Manages file watching and basic file processing.
- **Description**: Initializes family members, sets up file watching, processes Markdown files upon creation or modification.
- **Required Changes**: Integrate `api_tool.py` to use different LLMs based on content analysis and operational needs.

## Directory: `FamilyCrewAI/tasks`

### `md_tasks.py`

- **Current State**: Contains logic to parse Markdown files.
- **Description**: Defines tasks that direct member actions based on Markdown content.
- **Required Changes**: Update to support dynamic decision-making regarding LLM use.

## Directory: `FamilyCrewAI/tools`

### Files and Descriptions

#### `file_tool.py`

- **Current State**: Provides file manipulation capabilities.
- **Description**: Encapsulates file operations like reading, writing, and watching.
- **Required Changes**: None, unless additional file operations are needed.

#### `api_tool.py`

- **Current State**: Handles predefined API interactions.
- **Description**: Manages requests to various LLMs including local, OpenAI, and Hugging Face models.
- **Required Changes**: Update to dynamically choose APIs based on operational criteria.

#### `env_tool.py`

- **Current State**: Manages environment variables.
- **Description**: Loads and handles environmental configurations.
- **Required Changes**: Update to manage new variables for Hugging Face API.

## Directory: `FamilyCrewAI/logs`

### `logger.py`

- **Current State**: Basic logging functionality.
- **Description**: Logs system activities, errors, and operational data.
- **Required Changes**: Enhance to log detailed decision processes regarding LLM selection.

## Directory: `FamilyCrewAI/tests`

### Files and Descriptions

#### `test_agents.py`

- **Current State**: Tests basic functionalities of agents.
- **Description**: Unit tests for behaviors and functionalities of agents.
- **Required Changes**: Include tests for new capabilities and LLM integration.

#### `test_tools.py`

- **Current State**: Tests tool functionalities.
- **Description**: Tests all tools including file and API tools.
- **Required Changes**: Expand to test dynamic API selection logic.

## Conclusion

This document outlines necessary updates to each component of the FamilyAI project. These updates will support intelligent LLM selection and ensure robust and scalable operations, aligning with the project's advanced requirements.
