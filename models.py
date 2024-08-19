# models.py
from pydantic import BaseModel

class ScheduleRequest(BaseModel):
    transcript_pdf: bytes

# routes.py
from fastapi import FastAPI, UploadFile, File
from .utils import scrape_transcript
from .llama_interface import generate_schedule
from .models import ScheduleRequest

app = FastAPI()

@app.post("/create-schedule/")
async def create_schedule(file: UploadFile = File(...)):
    # Scrape the PDF transcript
    transcript_data = scrape_transcript(file.file)

    # Load course and degree requirements from the "data" folder
    with open("data/courses.json") as f:
        courses = json.load(f)
    with open("data/prerequisites.json") as f:
        prerequisites = json.load(f)
    with open("data/degree_requirements.json") as f:
        degree_requirements = json.load(f)

    # Generate the LLM prompt
    prompt = f"Hello, please create a schedule for a student. {transcript_data} {courses} {prerequisites} {degree_requirements}"
    schedule = generate_schedule(prompt)

    return {"schedule": schedule}
