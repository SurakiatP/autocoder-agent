# main.py

import os
from agents.code_writer import generate_code
from agents.tester import generate_test
from agents.executor import run_code_and_tests
from agents.fixer import fix_code
from pathlib import Path

# You can replace this with dynamic input or read from a file
TASK_INPUT = """
Write a Python function to check if a string is a palindrome.
"""

def save_output(code: str, test: str, result: str):
    """
    Save generated code, test case, and execution result into the outputs/ directory.
    """
    Path("outputs").mkdir(parents=True, exist_ok=True)

    with open("outputs/generated_code.py", "w", encoding="utf-8") as f:
        f.write(code)

    with open("outputs/test_generated.py", "w", encoding="utf-8") as f:
        f.write(test)

    with open("outputs/result_log.md", "w", encoding="utf-8") as f:
        f.write(result)

def main():
    print("📨 Received task: ", TASK_INPUT.strip())

    # Step 1: Generate Python function from natural language task
    print("🧠 Generating code from Agent ...")
    code = generate_code(task=TASK_INPUT)

    # Step 2: Generate test cases for the function
    print("🧪 Generating test cases ...")
    test_code = generate_test(function_code=code)

    # Step 3: Run the function and test it
    print("⚙️ Executing code and tests ...")
    result, success = run_code_and_tests(code, test_code)

    # Step 4: If test failed, use fixer agent to debug and rerun
    if not success:
        print("🛠 Test failed → invoking fixer agent ...")
        fixed_code = fix_code(task=TASK_INPUT, code=code, error_log=result)
        result_fixed, success_fixed = run_code_and_tests(fixed_code, test_code)

        # Save fixed result
        save_output(fixed_code, test_code, result_fixed)

        if success_fixed:
            print("✅ Bug fixed successfully!")
        else:
            print("❌ Bug remains after fix attempt.")
    else:
        print("✅ Tests passed successfully!")
        save_output(code, test_code, result)

if __name__ == "__main__":
    main()
