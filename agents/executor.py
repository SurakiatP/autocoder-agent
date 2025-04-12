import subprocess
import tempfile
import os

def run_code_and_tests(code: str, test_code: str, timeout: int = 5) -> tuple[str, bool]:
    """
    Run the generated Python code and test code in an isolated temp environment.

    Args:
        code (str): Python function code.
        test_code (str): Python test code (using assert).
        timeout (int): Maximum allowed time in seconds.

    Returns:
        Tuple[str, bool]: (execution result log, passed flag)
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        code_path = os.path.join(temp_dir, "generated_code.py")
        test_path = os.path.join(temp_dir, "test_code.py")

        # Save function code
        with open(code_path, "w", encoding="utf-8") as f:
            f.write(code)

        # Add import statement before test code
        full_test_code = f"from generated_code import *\n\n{test_code}"
        with open(test_path, "w", encoding="utf-8") as f:
            f.write(full_test_code)

        try:
            # Run test file with subprocess
            result = subprocess.run(
                ["python", test_path],
                capture_output=True,
                text=True,
                timeout=timeout
            )

            output = result.stdout + "\n" + result.stderr
            passed = result.returncode == 0

            return output.strip(), passed

        except subprocess.TimeoutExpired:
            return "[Timeout] Test execution exceeded limit.", False
        except Exception as e:
            return f"[Execution Error] {e}", False
