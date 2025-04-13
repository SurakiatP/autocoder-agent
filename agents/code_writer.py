import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.model_router import route_task
from utils.prompt_loader import load_prompt, clean_code_response

def generate_code(task: str, max_tokens: int = 512) -> str:
    """
    Generate Python function code from a natural language task description.

    Args:
        task (str): Instruction like "Write a function to reverse a string."
        max_tokens (int): Maximum tokens to generate.

    Returns:
        str: The generated Python function code.
    """
    prompt = load_prompt("prompts/code_generation.txt", {"task": task.strip()})
    response = route_task(task_type="code_generation", prompt=prompt, max_tokens=max_tokens)
    code = clean_code_response(response)

    return code