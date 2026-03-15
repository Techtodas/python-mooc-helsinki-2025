# write your solution here
def ask_user():
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    return student_info, exercise_data

def student_names(filename):
    names = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(';')
            if parts[0] == "id":
                continue
            names[parts[0]] = parts[1] + " " + parts[2]
    return names

def exercises(filename):
    exercise_sum = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(';')
            name = parts[0]
            numbers = parts[1:]
            if name == "id":
                continue

            total = 0
            for number in numbers:
                total += int(number)
            exercise_sum[name] = total
    return exercise_sum

def main():
    student_info, exercise_data = ask_user()
    students = student_names(student_info)
    total_score = exercises(exercise_data)
 
    for student_id in students:
        name = students[student_id]
        score = total_score.get(student_id, 0)
        print(name, score)
        
main()