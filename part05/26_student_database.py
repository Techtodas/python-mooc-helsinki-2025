# Write your solution here
def add_student(students, name):
    if name not in students:
        students[name] = {}

def print_student(students, name):
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        courses = students[name]
        if len(courses) == 0:
            print(f"{name}:")
            print(" no completed courses")
            return

        print(f"{name}:")
        print(f" {len(courses)} completed courses:")

        total_grade = 0
        for course, grade in courses.items():
            total_grade+=grade
            print(" ", course, grade)
            
        average = total_grade/len(courses)
        print(" average grade", average)

def add_course(students, name, course):
    courses = students[name]
    course_name, grade = course
    if grade == 0:
        return
    
    if course_name in courses:
        old = courses[course_name]
        if grade > old:
            courses[course_name] = grade
    else:
        courses[course_name] = grade

def summary(students):
    highest_count = 0
    highest_name = ""
    best_avg = -1
    best_avg_name = ""

    for name in students:
        courses = students[name]
        course_count = len(courses)

        if course_count > highest_count:
            highest_count = course_count
            highest_name = name

        total = 0
        for course, grade in courses.items():
            total+=grade

        if course_count > 0:
            average = total/course_count
            if average > best_avg:
                best_avg = average
                best_avg_name = name

    print(f"students {len(students)}")
    print(f"most courses completed {highest_count} {highest_name}")
    print(f"best average grade {best_avg} {best_avg_name}")
    

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)