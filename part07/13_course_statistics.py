# Write your solution here
import json, urllib.request


def retrieve_all():
    my_req = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_req.read()
    courses = json.loads(data)

    active_course = []
    for i in courses:
        if i["enabled"]:
            active_course.append((i["fullName"], i["name"], i["year"], sum(i["exercises"])))

    return active_course


def retrieve_course(course_name: str):
    my_req = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_req.read()
    course_details = json.loads(data)

    course_stats = {
    'weeks': 0,
    'students': 0,
    'hours': 0,
    'hours_average': 0,
    'exercises': 0,
    'exercises_average': 0
    }

    highest_students = 0
    hour_total = 0
    exercises = 0
    for key, value in course_details.items():
        if value["students"] > highest_students:
            highest_students = value["students"]
        
        hour_total += value["hour_total"]
        exercises += value["exercise_total"]
            
    course_stats["weeks"] = len(course_details)
    course_stats["students"] = highest_students
    course_stats["hours"] = hour_total
    course_stats["hours_average"] = hour_total//highest_students
    course_stats["exercises"] = exercises
    course_stats["exercises_average"] = exercises//highest_students

    return course_stats