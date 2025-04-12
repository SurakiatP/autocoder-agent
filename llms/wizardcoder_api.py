# llms/wizardcoder_api.py

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_wizardcoder():
    model_id = "WizardLM/WizardCoder-Python-34B-V1.0"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    return tokenizer, model

def generate_wizardcoder(prompt: str, max_tokens: int = 512):
    tokenizer, model = load_wizardcoder()
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=max_tokens)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
