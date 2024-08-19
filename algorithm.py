from typing import List, Dict

def check_prerequisites(course, completed_courses):
    return all(prereq in completed_courses for prereq in course['prerequisites'])

def is_course_available(course, semester):
    return semester in course['available_semesters']

def generate_schedule(data):
    schedule = {}
    completed_courses = set()
    total_semesters = data['total_semesters']
    break_semesters = set(data['break_semesters'])

    for semester in range(1, total_semesters + 1):  # Adjust based on total semesters
        if semester in break_semesters:
            schedule[semester] = []  # No courses in this semester
            continue

        schedule[semester] = []
        for course in data['available_courses']:
            if (is_course_available(course, semester) and 
                check_prerequisites(course, completed_courses) and
                course['course_id'] not in completed_courses):
                
                schedule[semester].append(course['course_id'])
                completed_courses.add(course['course_id'])

    return schedule
