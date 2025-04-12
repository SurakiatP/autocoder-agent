import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from llms.ollama_client import generate_with_ollama

def route_task(task_type: str, prompt: str, max_tokens: int = 512) -> str:
    """
    Route a task to the appropriate LLM backend (currently using Ollama for all).

    Args:
        task_type (str): The type of task (e.g., 'code_generation', 'test_generation', 'bug_fixing').
        prompt (str): The prompt to send to the model.
        max_tokens (int): Max number of tokens to generate.

    Returns:
        str: The generated output from the model.
    """
    # Dev Mode: use Ollama for all task types
    return generate_with_ollama(prompt, max_tokens=max_tokens)
