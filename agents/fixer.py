from agents.model_router import route_task
from utils.prompt_loader import load_prompt, clean_code_response

def fix_code(task: str, code: str, error_log: str, max_tokens: int = 512) -> str:
    """
    Use LLM to analyze and fix a Python function based on an error log.

    Args:
        task (str): The original task/instruction.
        code (str): The buggy code that failed testing.
        error_log (str): The error message or test failure log.

    Returns:
        str: The corrected Python function code.
    """
    prompt = load_prompt("prompts/bug_fixing.txt", {
        "task": task.strip(),
        "code": code.strip(),
        "error_log": error_log.strip()
    })

    response = route_task(task_type="bug_fixing", prompt=prompt, max_tokens=max_tokens)
    fixed_code = clean_code_response(response)
    return fixed_code.strip()