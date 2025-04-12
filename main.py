from agents.code_writer import generate_code
from agents.tester import generate_test
from agents.executor import run_code_and_tests
from agents.fixer import fix_code
from pathlib import Path

# Explain the meaning of (to be able to)
TASK_INPUT = """
Write a Python function to check if a string is a palindrome.
"""

def save_output(code: str, test: str, result: str):
    Path("outputs").mkdir(parents=True, exist_ok=True)

    with open("outputs/generated_code.py", "w", encoding="utf-8") as f:
        f.write(code)

    with open("outputs/test_generated.py", "w", encoding="utf-8") as f:
        f.write(test)

    with open("outputs/result_log.md", "w", encoding="utf-8") as f:
        f.write(result)

def main():
    print("Task received:")
    print(TASK_INPUT.strip())

    # generate code
    code = generate_code(task=TASK_INPUT)
    print("Code generated.")

    # generate_test
    test_code = generate_test(function_code=code)
    print("Test cases generated.")

    # run code and test
    result, passed = run_code_and_tests(code, test_code)
    print("Test executed.")

    if passed:
        print("(/) All tests passed on first attempt.")
        save_output(code, test_code, result)
    else:
        print("(!) Test failed. Attempting to fix...")
        fixed_code = fix_code(task=TASK_INPUT, code=code, error_log=result)
        fixed_result, fixed_passed = run_code_and_tests(fixed_code, test_code)

        save_output(fixed_code, test_code, fixed_result)

        if fixed_passed:
            print("(/) Bug fixed. All tests passed.")
        else:
            print("(!) Bug still exists after fix attempt.")

if __name__ == "__main__":
    main()
