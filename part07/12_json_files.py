# Write your solution here
import json 

def print_persons(filename: str):
    with open(filename) as f:
        data = f.read()

    students = json.loads(data)

    for i in students:
        print(f"{i["name"]} {i["age"]} years ({", ".join(x for x in i["hobbies"])})")