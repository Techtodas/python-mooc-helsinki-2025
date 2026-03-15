# tee ratkaisu tänne
def ask_user():
    if True:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_data = input("Exam points: ")
        course = input("Course information: ")
    else:
        student_info = "students2.csv"
        exercise_data = "exercises2.csv"
        exam_data = "exam_points2.csv"
        course = "course2.txt"

    return student_info, exercise_data, exam_data, course

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


def course_info(filename):
    course = []
    divider = ""

    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(":")
            course.append(parts[1])
            


    course_details = f"{course[0]},{course[1]} credits"
    divider += "="*(len(course_details) - 1)

    return course_details, divider

def main():
    student_info, exercise_data, exam_data, course = ask_user()
    students = student_names(student_info)
    total_score = exercises(exercise_data)
    total_points = exam_points(exam_data)
    course_details, divider = course_info(course)
    
    with open("results.txt", "w") as txt_file, open("results.csv", "w") as csv_file:
        txt_file.write(course_details+"\n")
        txt_file.write(divider+"\n")
        #csv_file.write(course_details+"\n")
        #csv_file.write(divider+"\n")
        txt_file.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
        #csv_file.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
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
            



            txt_file.write(f"{name:30}{score:<10}{exercise_points:<10}{points:<10}{final_score:<10}{final_grade:<10}\n")
            csv_file.write(f"{student_id};{name};{final_grade}\n")

main()