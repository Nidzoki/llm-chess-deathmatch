# llm-chess-deathmatch

### Idea: Last standing LLM wins

A platform to benchmark and compare various Large Language Models (LLMs) in chess matches. The ultimate goal is to determine the "last standing LLM" by simulating chess tournaments.

## Features:
*   Support for multiple LLM agents (Gemini, Cohere, Groq, Reka, YouChat).
*   Core logic for conducting chess matches and tournaments.
*   Utilities for PGN (Portable Game Notation) handling and move parsing.
*   Modular agent architecture allowing for easy integration of new LLMs.

## Installation:
To set up the project, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/llm-chess-deathmatch.git
    cd llm-chess-deathmatch
    ```
2.  **Set up the virtual environment**:
    Use the provided script to create and activate a Python virtual environment and install dependencies.
    ```bash
    .\enviroment_setup\setup_venv.bat
    ```
    This script will create a `venv` directory, install all required packages from `requirements/requirements.txt`, and upgrade pip.
3.  **Activate the virtual environment**:
    ```bash
    .\enviroment_setup\activate_venv.bat
    ```

## Usage:
After setting up the environment, you can run the chess deathmatch by executing Python scripts in the `core` or `examples` directories. Refer to specific examples or documentation within those directories for detailed usage.

## Supported Agents:
*   Gemini
*   Cohere
*   Groq
*   Reka
*   YouChat

## Contributing:
Contributions are welcome! Please refer to the `TODO.md` for current tasks or open an issue to discuss new features or bug fixes.

## License:
This project is licensed under the terms of the [LICENSE](LICENSE) file.