import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.code_writer import generate_code
from agents.tester import generate_test
from agents.executor import run_code_and_tests
from agents.fixer import fix_code
from utils.prompt_loader import clean_code_response

st.set_page_config(page_title="AutoCoder Agent", layout="wide")
st.title("🤖 AutoCoder Agent")
st.subheader("Give me a coding task in plain English, and I’ll write, test, and fix the code for you!")

user_input = st.text_area("Enter your Python task", height=150,  placeholder="e.g., Write a function to check if a number is prime")

if st.button("🚀 Run Agent") and user_input:
    with st.spinner("Generating code..."):
        code = generate_code(user_input)
        code = clean_code_response(code)
        st.code(code, language="python", line_numbers=True)

    with st.spinner("Generating test cases..."):
        test_code = generate_test(code)
        test_code = clean_code_response(test_code)
        st.code(test_code, language="python")

    with st.spinner("Running tests..."):
        result, passed = run_code_and_tests(code, test_code)
        st.text_area("Test Results", result, height=150)

    if not passed:
        st.warning("(!) Test failed. Trying to fix...")
        for attempt in range(3):
            with st.spinner(f"Fixing... Attempt {attempt + 1}"):
                code = fix_code(user_input, code, result)
                code = clean_code_response(code)
                result, passed = run_code_and_tests(code, test_code)
                if passed:
                    break

        st.subheader("(.) Fixed Code")
        st.code(code, language="python")

        st.subheader("(.) Fixed Test Result")
        st.text_area("", result, height=150)

        if not passed:
            st.error("(!) Still failing after auto-fix.")
        else:
            st.success("✅ Bug fixed. All tests passed.")
    else:
        st.success("✅ All tests passed on first attempt")

