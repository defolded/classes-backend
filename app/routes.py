from fastapi import APIRouter, Form, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from .model import query_llm

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def generate(prompt: str = Form(...)):
    query_llm_response = await query_llm(prompt)
    return JSONResponse({"content": query_llm_response.content})