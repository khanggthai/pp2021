import domain
from input import *


def options():
    print("""
    Choose?
    1. Add a student
    2. Add a course
    3. List students in class
    4. List courses
    5. Make a student learn
    6. Mark a student
    7. List student's GPA
    """)
    option = int(input())
    return option


def student_management():
    print("What now?")
    while True:
        option = options()
        if option == 1:
            add_student_info(c1ass)
        elif option == 2:
            add_course_info(courses)
        elif option == 3:
            display_student(c1ass)
        elif option == 4:
            display_courses(courses)
        elif option == 5:
            enroll()
        elif option == 6:
            mark_student()
        elif option == 7:
            for student in c1ass:
                GPA_calculate(student)
            display_GPA(c1ass, courses)
        else:
            print("Try again")
