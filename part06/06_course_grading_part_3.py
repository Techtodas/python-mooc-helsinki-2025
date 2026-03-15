# write your solution here
def ask_user():
    if True:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_data = input("Exam points: ")
    else:
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_data = "exam_points1.csv"

    return student_info, exercise_data, exam_data

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

def exam_points(filename):
    points_sum = {}
    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(';')
            name = parts[0]
            numbers = parts[1:]
            if name == 'id':
                continue

            total = 0
            for number in numbers:
                total += int(number)
            points_sum[name] = total
    return points_sum


def main():
    student_info, exercise_data, exam_data = ask_user()
    students = student_names(student_info)
    total_score = exercises(exercise_data)
    total_points = exam_points(exam_data)
 
    print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
    for student_id in students:
        final_grade = 0
        name = students[student_id]
        score = total_score.get(student_id, 0)
        points = total_points.get(student_id, 0)
        exercise_points = score // 4
        final_score = points + exercise_points

        if final_score <= 14:
            final_grade = 0
        elif final_score <= 17:
            final_grade = 1
        elif final_score <= 20:
            final_grade = 2
        elif final_score <= 23:
            final_grade = 3
        elif final_score <= 27:
            final_grade = 4
        else:
            final_grade = 5

        print(f"{name:30}{score:<10}{exercise_points:<10}{points:<10}{final_score:<10}{final_grade:<10}")


main()