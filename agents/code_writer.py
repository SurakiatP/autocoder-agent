# agents/code_writer.py

from agents.model_router import route_task

def generate_code(task: str, max_tokens: int = 512) -> str:
    """
    Generate Python code based on a natural language task description.

    Args:
        task (str): The natural language instruction for the code task.
        max_tokens (int): Maximum number of tokens to generate from the model.

    Returns:
        str: The generated Python function code as a string.
    """

    # Define the prompt format for code generation
    prompt = (
        "You are a helpful coding assistant. Write a clean and working Python function for the following task:\n\n"
        f"Task: {task.strip()}\n\n"
        "Please provide only the function code without explanations."
    )

    # Use the model router to send to WizardCoder (via task_type)
    response = route_task(task_type="code_generation", prompt=prompt, max_tokens=max_tokens)

    return response.strip()
