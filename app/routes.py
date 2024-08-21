from fastapi import APIRouter, Form, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from .llama_interface import query_llm

import marqo
import pprint

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

# Initialize Marqo client
mq = marqo.Client(url="http://localhost:8882")

def query_courses(query_dict):
    index_name = "university-courses"
    
    # Perform the search with weighted queries
    results = mq.index(index_name).search(q=query_dict)
    
    # Format or return results as needed
    return results

class QueryModel(BaseModel):
    query: str

@router.post("/generate")
async def generate(prompt: str = Form(...)):
    # Example query dictionary based on the user prompt
    query_dict = {
        prompt: 1.0,
        "Advanced integration techniques": 0.5  # Adjust this based on your use case
    }
    
    # Get course results based on the query
    results = query_courses(query_dict)
    
    # Return the results to the user
    return {"response": results}