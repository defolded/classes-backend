from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
	filename="Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",
)

def query_llm(prompt: str) -> str:
    # Create a chat completion using the Llama model
    response = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    # Extract the content of the response from the Llama model
    return response['choices'][0]['message']['content']