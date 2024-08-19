from fastapi import FastAPI
from schemas import ScheduleRequest
from algorithm import generate_schedule

app = FastAPI()

@app.post("/generate_schedule/")
def generate_schedule_endpoint(schedule_request: ScheduleRequest):
    data = schedule_request.dict()
    schedule = generate_schedule(data)
    return schedule
