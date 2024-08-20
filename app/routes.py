from fastapi import APIRouter
from pydantic import BaseModel
import json
from .llama_interface import query_llm  # Make sure this import is correct

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

def load_courses():
    with open("data/courses.json") as f:
        courses_data = json.load(f)
    return courses_data

def filter_math_courses(courses_data):
    return [course for course in courses_data["courses"] if course["department"] == "Mathematics"]

def format_courses_for_prompt(courses):
    return [{"course_id": course["course_id"], "course_name": course["course_name"]} for course in courses]

def filter_llm_response(response: str, math_courses):
    # Extract the valid course names from the response
    valid_course_names = {course['course_name']: course for course in math_courses}
    
    # Split the response into lines and filter out any lines that aren't in the provided data
    filtered_lines = []
    for line in response.split("\n"):
        course_name = line.split(":")[-1].strip()
        if course_name in valid_course_names:
            filtered_lines.append(line)
    
    # Reconstruct the response from filtered lines
    return "\n".join(filtered_lines)


@router.post("/generate")
async def generate_prompt(request: PromptRequest):
    courses_data = load_courses()

    # Normalize and check the prompt for specific keywords
    prompt_text = request.prompt.strip().lower()

    if "math courses" in prompt_text:
        # User is asking for math courses
        math_courses = filter_math_courses(courses_data)
        course_list = [{"course_id": course["course_id"], "course_name": course["course_name"]} for course in math_courses]
        response = course_list

    elif "prerequisites for" in prompt_text:
        # User is asking for prerequisites
        course_id = prompt_text.split()[-1].upper()  # Extract the last word as course ID
        course = next((course for course in courses_data["courses"] if course["course_id"] == course_id), None)

        if course:
            prerequisites = course["prerequisites"]
            if prerequisites:
                prereq_names = [c["course_name"] for c in courses_data["courses"] if c["course_id"] in prerequisites]
                response = {
                    "course_id": course["course_id"],
                    "course_name": course["course_name"],
                    "prerequisites": prereq_names
                }
            else:
                response = {
                    "course_id": course["course_id"],
                    "course_name": course["course_name"],
                    "prerequisites": "None"
                }
        else:
            response = {"error": "Course not found."}

    else:
        # If the prompt doesn't match any of the expected patterns, use the LLaMA model
        response = query_llm(request.prompt)

    return {"response": response}
