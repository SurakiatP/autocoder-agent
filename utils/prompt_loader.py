def load_prompt(file_path: str, context: dict) -> str:
    """
    Load a prompt template from a .txt file and inject variables using .format().

    Args:
        file_path (str): Path to the template file (e.g., prompts/code_generation.txt)
        context (dict): Key-value pairs to replace in the template

    Returns:
        str: Prompt string with all placeholders filled
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            template = f.read()
        return template.format(**context)
    except KeyError as e:
        raise ValueError(f"Missing variable in context: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file not found: {file_path}")
