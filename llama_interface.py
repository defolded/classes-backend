# llama_interface.py
from transformers import pipeline

def generate_schedule(prompt: str, model_name: str = "Meta-Llama-3.1-8B-Instruct"):
    generator = pipeline('text-generation', model=model_name)
    output = generator(prompt, max_length=500)
    return output[0]['generated_text']
