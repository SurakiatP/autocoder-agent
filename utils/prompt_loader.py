# utils/prompt_loader.py

def load_prompt(file_path: str, context: dict) -> str:
    """
    Load a prompt template from a file and fill it with provided context variables.

    Args:
        file_path (str): Path to the prompt template file (e.g., prompts/code_generation.txt)
        context (dict): Dictionary of placeholder values (e.g., {"task": "..."})

    Returns:
        str: The rendered prompt string
    """
    with open(file_path, "r", encoding="utf-8") as f:
        template = f.read()

    return template.format(**context)
