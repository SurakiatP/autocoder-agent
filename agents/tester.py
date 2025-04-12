from agents.model_router import route_task
from utils.prompt_loader import load_prompt

def generate_test(function_code: str, max_tokens: int = 512) -> str:
    """
    Generate test cases for a provided function using LLM.
    """
    prompt = load_prompt(
        "prompts/test_generation.txt",
        context={"function_code": function_code.strip()}
    )

    return route_task(task_type="test_generation", prompt=prompt, max_tokens=max_tokens).strip()
