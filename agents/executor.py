# agents/executor.py

import subprocess
import tempfile
import os

def run_code_and_tests(code: str, test_code: str, timeout: int = 5) -> tuple[str, bool]:
    """
    Run the generated Python code and test cases in an isolated temp environment.

    Args:
        code (str): The Python function code.
        test_code (str): The Python test code using assert statements.
        timeout (int): Max seconds to allow code execution.

    Returns:
        Tuple[str, bool]: (Execution result logs, Test pass status)
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        code_file_path = os.path.join(temp_dir, "generated_code.py")
        test_file_path = os.path.join(temp_dir, "test_code.py")

        # Save function code
        with open(code_file_path, "w", encoding="utf-8") as f:
            f.write(code)

        # Combine test code + import statement to call the function
        test_full_code = f"from generated_code import *\n\n{test_code}"

        # Save test code
        with open(test_file_path, "w", encoding="utf-8") as f:
            f.write(test_full_code)

        try:
            # Run test code
            result = subprocess.run(
                ["python", test_file_path],
                capture_output=True,
                text=True,
                timeout=timeout
            )

            output = result.stdout + "\n" + result.stderr
            passed = result.returncode == 0  # 0 = success

            return output.strip(), passed

        except subprocess.TimeoutExpired:
            return "[⏰ Timeout] Test execution exceeded the time limit.", False
        except Exception as e:
            return f"[💥 Exception] {str(e)}", False
