from agents.model_router import route_task
from utils.prompt_loader import load_prompt

def fix_code(task: str, code: str, error_log: str, max_tokens: int = 512) -> str:
    """
    Use LLM to analyze and fix the given code based on the error log.
    """
    prompt = load_prompt(
        "prompts/bug_fixing.txt",
        context={
            "task": task.strip(),
            "code": code.strip(),
            "error_log": error_log.strip()
        }
    )

    return route_task(task_type="bug_fixing", prompt=prompt, max_tokens=max_tokens).strip()
