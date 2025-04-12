from agents.model_router import route_task
from utils.prompt_loader import load_prompt

def generate_code(task: str, max_tokens: int = 512) -> str:
    """
    Generate Python code based on a natural language task description.
    """
    prompt = load_prompt(
        "prompts/code_generation.txt",
        context={"task": task.strip()}
    )

    response = route_task(task_type="code_generation", prompt=prompt, max_tokens=max_tokens)
    return response.strip()
