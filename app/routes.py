from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from .model import query_llm

router = APIRouter()

@router.post("/generate")
def generate(prompt: str = Form(...)):
    query_llm_response = query_llm(prompt)
    
    # Assuming query_llm_response is an AIMessage, extract its content
    content = query_llm_response.content if hasattr(query_llm_response, 'content') else str(query_llm_response)
    
    return JSONResponse({"content": content})