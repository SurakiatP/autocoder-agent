# AutoCoder Agent

AutoCoder Agent is an Agentic AI project that automatically generates Python code from natural language tasks, creates corresponding test cases, executes the code, and iteratively fixes any bugs until all tests pass. The project is designed to showcase a full end-to-end automated coding pipeline using various AI agents.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Workflow](#workflow)
- [Installation](#installation)
- [Usage](#usage)
- [Mermaid Diagram](#mermaid-diagram)
- [License](#license)

---

## Features

- **Automated Code Generation**: Converts natural language prompts to working Python functions.
- **Test Case Generation**: Automatically produces assert-based test cases based on the generated code.
- **Code Execution & Validation**: Runs the generated code with tests to ensure correctness.
- **Bug Fixing Loop**: Utilizes an AI agent to analyze errors and iteratively fix bugs until tests pass.
- **Interactive UI**: A Streamlit interface is provided for a real-time interactive demonstration.
- **Modular Design**: The system is designed with separate agents for code writing, testing, execution, and fixing, making it easy to extend or switch LLM backends.

---

## Project Structure

```
autocoder-agent/ 
├── main.py                         # Entry point to run the full agent loop 
├── requirements.txt                # Python dependencies 
├── agents/                         # Agent components 
│ ├── code_writer.py                # Generates code from a task prompt 
│ ├── tester.py                     # Generates test cases for the function 
│ ├── executor.py                   # Executes the function and tests 
│ ├── fixer.py                      # Analyzes errors and fixes the code via LLM 
│ └── model_router.py               # Routes tasks to the LLM backend (currently using Ollama) 
├── llms/                           # LLM interface modules 
│ └── ollama_client.py              # Calls Ollama via HTTP API 
├── prompts/                        # Prompt templates for each agent 
│ ├── code_generation.txt           # Prompt for writing code 
│ ├── test_generation.txt           # Prompt for writing tests (only returns assert statements) 
│ └── bug_fixing.txt                # Prompt for fixing code based on error logs 
├── utils/                          # Helper functions 
│ └── prompt_loader.py              # Loads and fills prompt templates with context; also contains clean_code_response() 
├── outputs/                        # Generated outputs (auto-saved after running main.py) 
│ ├── generated_code.py 
│ ├── test_generated.py 
│ └── result_log.md 
└── ui/                             # Streamlit UI for interactive usage 
    └── streamlit_app.py
```


---

## Workflow

The AutoCoder Agent follows an end-to-end process:

1. **User Prompt**: The user provides a natural language task (e.g., "Write a function to check if a string is a palindrome.").
2. **Code Writer Agent**: Generates Python code for the task using an LLM backend (via Ollama in Dev Mode).
3. **Test Generator Agent**: Automatically creates assert-based test cases for the generated code.
4. **Code Executor**: Runs the generated code and test cases in an isolated environment to capture the output and any errors.
5. **Fixer Agent**: If tests fail, analyzes the error log and iteratively fixes the code. This process repeats up to a defined maximum number of attempts.
6. **Final Output**: The final version of the code (and tests) that pass all test cases are saved and displayed.

---

## Usage

### Running on the Command Line

1. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```
2. **Start the LLM Backend (Ollama)**:

    Make sure to run Ollama with your desired model, for example:
    ```bash
    ollama run wizardcoder
    ```
    This ensures that the LLM is available via HTTP (default URL: http://localhost:11434).

3. **Run the Agent Pipeline**:
    ```bash
    python main.py
    ```

    - The system will process the prompt, generate code and tests, execute them, and, if necessary, try to fix bugs through iterative attempts.
    - Output files will be saved automatically in the outputs/ directory.

## Running with the Streamlit UI
1. **Start the LLM Backend (Ollama)**:

    ```bash
    ollama run wizardcoder
    ```
2. **Run the Streamlit App**:

    ```bash
    streamlit run ui/streamlit_app.py
    ```
    - This opens a browser window at http://localhost:8501 where you can enter your task, run the agent interactively, and view the generated code, tests, and results.
    
## Mermaid Diagram

Below is a Mermaid script representing the full workflow of the AutoCoder Agent:

    ```bash
    flowchart TD
        A[User Prompt<br>Enter natural language task] --> B[ Code Writer Agent<br>Generate function code]
        B --> C[ Test Generator Agent<br>Create assert-based test cases]
        C --> D[ Code Executor<br>Run code and tests, capture errors]
        D --> E{Tests Passed?}
        E -- Yes --> F[Success<br>Display final code and results]
        E -- No --> G[ Fixer Agent<br>Analyze error log and fix code]
        G --> H{Retry attempts left?}
        H -- Yes --> D
        H -- No --> I[Failure<br>Output error log and failed fix attempts]
    ```
This diagram can be used in presentations and documentation to clearly illustrate the project workflow.

---
## License
This project is licensed under the MIT License.

---
## Conclusion
AutoCoder Agent demonstrates an end-to-end AI-powered coding pipeline, integrating code generation, test case creation, and automatic bug fixing into a unified system. The modular design allows for seamless switching of LLM backends and easy extension for future enhancements.
---
## Project Author

| Name           | Contact Information                                                  |
|----------------|----------------------------------------------------------------------|
| **Surakiat P.** |                                                                      |
| 📧 Email       | [surakiat.0723@gmail.com](mailto:surakiat.0723@gmail.com)   |
| 🔗 LinkedIn    | [linkedin.com/in/surakiat](https://www.linkedin.com/in/surakiat-kansa-ard-171942351/)     |
| 🌐 GitHub      | [github.com/SurakiatP](https://github.com/SurakiatP)                 |
