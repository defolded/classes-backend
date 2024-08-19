from pydantic import BaseModel
from typing import List, Dict

class Course(BaseModel):
    course_id: str
    name: str
    credits: int
    prerequisites: List[str]
    available_semesters: List[int]

class ScheduleRequest(BaseModel):
    graduation_year: int
    degree_requirements: Dict[str, int]  # e.g., {"core": 30, "electives": 15}
    available_courses: List[Course]
    personal_time: Dict[str, List[str]]  # e.g., {"Monday": ["09:00-12:00"], "Wednesday": []}
    break_semesters: List[int]  # Semesters where no classes will be taken
    total_semesters: int  # Total number of semesters available (e.g., 6 for transfer students)
