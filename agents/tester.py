from agents.model_router import route_task
from utils.prompt_loader import load_prompt, clean_code_response

def generate_test(function_code: str, max_tokens: int = 512) -> str:
    """
    Generate test cases (assert statements) for the given function code.

    Args:
        function_code (str): The function code to be tested.
        max_tokens (int): Maximum tokens to generate.

    Returns:
        str: The generated test cases.
    """
    prompt = load_prompt("prompts/test_generation.txt", {"function_code": function_code.strip()})
    response = route_task(task_type="test_generation", prompt=prompt, max_tokens=max_tokens)
    test_code = clean_code_response(response)
    return test_code.strip()