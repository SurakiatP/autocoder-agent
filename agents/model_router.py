# agents/model_router.py

from llms.wizardcoder_api import generate_wizardcoder
from llms.deepseek_api import generate_deepseek
from llms.starcoder_api import generate_starcoder

def route_task(task_type: str, prompt: str, max_tokens: int = 512) -> str:
    """
    Select the appropriate LLM according to the task type and call it to generate the response message.

    Args:
        task_type (str): The type of task, e.g. 'code_generation', 'bug_fixing', 'test_generation'

        prompt (str): The prompt message to send to the LLM

        max_tokens (int): The number of tokens to generate

    Returns:
        str: The message from the appropriate LLM
    """

    if task_type == "code_generation":
        return generate_wizardcoder(prompt, max_tokens=max_tokens)

    elif task_type == "bug_fixing":
        return generate_deepseek(prompt, max_tokens=max_tokens)

    elif task_type == "test_generation":
        return generate_starcoder(prompt, max_tokens=max_tokens)

    else:
        raise ValueError(f"[!] Unknown task_type: {task_type}")
