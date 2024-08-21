import marqo
import json

# Initialize Marqo client
mq = marqo.Client(url="http://localhost:8882")

# Create the course index
mq.create_index("university-courses")

# Load course data from a JSON file (assuming it's stored in 'courses.json')
with open('data/courses.json', 'r') as f:
    courses = json.load(f)

# Add courses to the index
mq.index("university-courses").add_documents(
    [
        {
            "course_id": course["course_id"],
            "course_name": course["course_name"],
            "description": course["description"],
            "prerequisites": ", ".join(course["prerequisites"]) if course["prerequisites"] else "None"
        }
        for course in courses
    ],
    tensor_fields=["description", "course_name", "prerequisites"]
)
