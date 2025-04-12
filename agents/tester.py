import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.model_router import route_task
from utils.prompt_loader import load_prompt

def generate_test(function_code: str, max_tokens: int = 512) -> str:
    """
    Generate test cases (assert statements) for a given Python function.

    Args:
        function_code (str): Python function to test.
        max_tokens (int): Max tokens to generate.

    Returns:
        str: Python test code with assert statements.
    """
    prompt = load_prompt("prompts/test_generation.txt", {
        "function_code": function_code.strip()
    })

    response = route_task(task_type="test_generation", prompt=prompt, max_tokens=max_tokens)
    return response.strip()

