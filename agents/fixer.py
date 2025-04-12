# agents/fixer.py

from agents.model_router import route_task

def fix_code(task: str, code: str, error_log: str, max_tokens: int = 512) -> str:
    """
    Use an LLM to analyze the error log and suggest a fixed version of the Python code.

    Args:
        task (str): The original instruction/task.
        code (str): The original code that failed.
        error_log (str): The error message or failed test output.
        max_tokens (int): Max token length for LLM output.

    Returns:
        str: A revised version of the Python code that aims to fix the issue.
    """

    # Compose a detailed bug-fixing prompt
    prompt = (
        "You are an expert Python developer and debugger.\n"
        "Your job is to fix bugs in Python code based on the task, the original code, and the error log.\n\n"
        f"Task:\n{task.strip()}\n\n"
        f"Original Code:\n{code.strip()}\n\n"
        f"Error Log:\n{error_log.strip()}\n\n"
        "Return the corrected version of the code only, with no explanation."
    )

    # Send to DeepSeek-Coder via router
    fixed_code = route_task(task_type="bug_fixing", prompt=prompt, max_tokens=max_tokens)

    return fixed_code.strip()
