import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agents.code_writer import generate_code
from agents.tester import generate_test
from agents.executor import run_code_and_tests
from agents.fixer import fix_code

st.set_page_config(page_title="AutoCoder Agent", layout="wide")
st.title("AutoCoder Agent")
st.markdown("Give me a coding task in plain English, and I’ll write, test, and fix the code for you!")

task_input = st.text_area("Enter your Python task", height=150, placeholder="e.g., Write a function to check if a number is prime")

if st.button("Run Agent"):
    if not task_input.strip():
        st.warning("Please enter a task description.")
    else:
        with st.spinner("Generating code..."):
            code = generate_code(task_input)
        st.subheader("Generated Code")
        st.code(code, language="python")

        with st.spinner("Generating test cases..."):
            test_code = generate_test(code)
        st.subheader("Generated Test Cases")
        st.code(test_code, language="python")

        with st.spinner("Running test..."):
            result, passed = run_code_and_tests(code, test_code)
        st.subheader("Test Results")
        st.code(result)

        if passed:
            st.success("(/) All tests passed!")
        else:
            st.error("(!) Test failed. Trying to fix...")
            with st.spinner("Fixing the code..."):
                fixed_code = fix_code(task_input, code, result)
                fixed_result, fixed_passed = run_code_and_tests(fixed_code, test_code)

            st.subheader("(.) Fixed Code")
            st.code(fixed_code, language="python")

            st.subheader("(.) Fixed Test Result")
            st.code(fixed_result)

            if fixed_passed:
                st.success("(/) Bug fixed! All tests passed.")
            else:
                st.error("(!) Still failing after auto-fix.")
