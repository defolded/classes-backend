from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-8B-Instruct")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3.1-8B-Instruct")

def query_llm(prompt: str):
    # Encode the input prompt
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Generate a response
    outputs = model.generate(**inputs, max_length=150, top_k=50, top_p=0.95)
    
    # Decode the generated tokens to a string
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response
