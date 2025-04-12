# 🧪 Example Task: Check if a number is Prime

## 📌 Task Prompt

Write a Python function that returns True if a number is a prime number, and False otherwise.

---

## 🧠 Generated Code

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
---
## 🧪 Generated Test 

```bash
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(17) == True
assert is_prime(1) == False
assert is_prime(0) == False
```
---
## ⚙️ Execution Result
```bash
All tests passed.
```

## ✅ Final Status
> ✔ Code passed all tests on the first attempt – no bug fixing needed.

---

## 🗂 File References

|Component	|File|
|------------|:-------------|
|Generated Code	|outputs/generated_code.py|
|Generated Tests	|outputs/test_generated.py|
|Result Log	|outputs/result_log.md|
---
## 🧠 Notes
- This is a complete and successful example of the agent workflow.

- You can replace the task prompt with a new one and re-run main.py.