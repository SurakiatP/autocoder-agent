# agents/tester.py

from agents.model_router import route_task

def generate_test(function_code: str, max_tokens: int = 512) -> str:
    """
    Generate test cases (assert-based or unit test) for the provided Python function.

    Args:
        function_code (str): The Python function code to test.
        max_tokens (int): Maximum number of tokens to generate from the model.

    Returns:
        str: Python code for the generated test cases.
    """

    # Prompt for generating test cases
    prompt = (
        "You are a professional software tester.\n\n"
        "Given the following Python function, write 3-5 relevant test cases using assert statements.\n\n"
        "Function:\n"
        f"{function_code.strip()}\n\n"
        "Test code:\n"
    )

    # Send to StarCoder via router
    test_code = route_task(task_type="test_generation", prompt=prompt, max_tokens=max_tokens)

    return test_code.strip()
