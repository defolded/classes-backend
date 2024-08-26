from fastapi import APIRouter, Form, UploadFile, File
from fastapi.responses import JSONResponse
from .model import query_llm
from .parser import parse_transcript

router = APIRouter()

@router.post("/generate")
async def generate(prompt: str = Form(...), file: UploadFile = File(None)):
    transcript_classes = None
    
    if file is not None:
        file_path = f"data/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())

        transcript_classes = await parse_transcript(file_path)
    
    query_llm_response = query_llm(prompt, transcript_classes)
    content = query_llm_response.content if hasattr(query_llm_response, 'content') else str(query_llm_response)
    
    return JSONResponse({"content": content})
