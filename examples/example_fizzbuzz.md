# 🧪 Example Task: FizzBuzz Function

## 📌 Task Prompt
Write a Python function that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".


---

## 🧠 Generated Code

```python
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
```
---

## 🧪 Generated Test Cases

```python
import io
import sys

def capture_output(func):
    captured = io.StringIO()
    sys.stdout = captured
    func()
    sys.stdout = sys.__stdout__
    return captured.getvalue().splitlines()

output = capture_output(fizz_buzz)

assert output[2] == "Fizz"        # i = 3
assert output[4] == "Buzz"        # i = 5
assert output[14] == "FizzBuzz"   # i = 15
assert output[0] == "1"           # i = 1
```
---

## ⚙️ Execution Result
```bash
All tests passed.
```
---
## ✅ Final Status
> ✔ Code passed all test cases successfully – no bug fixing needed.
---
## 🗂 File References
|Component	|File|
|-----------|:-----------|
|Generated Code	| outputs/generated_code.py|
|Generated Tests	| outputs/test_generated.py|
|Result Log	| outputs/result_log.md|

---

## 🧠 Notes
- This example demonstrates the agent's ability to handle I/O-related tasks and verify output by capturing stdout.

- Good for evaluating agents on output-based code.