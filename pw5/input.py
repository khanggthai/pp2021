from domain import Student, Course, Mark
import math

c1ass = []
courses = []


def add_student_info(c1ass):
    print("Enter student info:")
    id = int(input("ID: "))
    name = str(input("Name:"))
    dob = str(input("Date of birth:"))
    student = Student(id, name, dob)
    c1ass.append(student)
    print("This student is added")

    open = open("student.tex", "a")
    open.write(f"{id} {name} {dob} \n")
    open.close()


def add_course_info(courses):
    print("Enter course info")
    id = int(input("ID:"))
    name = str(input("Name:"))
    credit = int(input("Number of credit: "))
    course = Course(id, name, credit)
    courses.append(course)
    print("This course is added")

    open = open("course.tex", "a")
    open.write(f"{id} {name} {credit} \n")
    open.close()


def display_student(c1ass):
    print(f"There are {len(c1ass)} students.")
    for i in c1ass:
        i.toString()


def display_courses(courses):
    print(f"The are {len(courses)} courses.")
    for s in courses:
        s.toString()


def searchId(list, id):
    for i in list:
        if i.getId() == id:
            print(i.getName())
            return i


def enroll():
    display_courses(courses)
    course = int(input("Which one?"))
    foundCourse = searchId(courses, course)

    display_student(c1ass)
    student = int(input("Which student? "))
    foundStudent = searchId(c1ass, student)

    mark = Mark(foundCourse, foundStudent)
    foundCourse.c1ass.append(mark)
    foundStudent.courses.append(mark)


def mark_student():
    display_courses(courses)
    course = int(input("Which course? "))
    found = Course(0, "Null")
    found = searchId(courses, course)
    for student in found.c1ass:
        print(f"Student: {student.Student}")
        mark = float(input("Input mark:"))
        student.Mark = math.floor(10* mark)/10


def display_marks(c1ass, courses):
    for c in courses:
        print(f"In course number {courses[c-1]}:")
        for student in c1ass:
            print(f"Student {student.name} has scored {student.Mark}")


def GPA_calculate(student):
    Course_Credit = 0
    Student_Mark = 0
    for course in student.c1ass:
        Student_Mark = Student_Mark + (course.Mark * course.Credit)
        Course_Credit = Course_Credit + course.Credit
    student.GPA = math.floor(10*gpa)/10


def display_GPA(c1ass, courses):
    for c in courses:
        print(f"In course number {courses[c-1]}:")
        for student in c1ass:
            print(f"Student {student.name} has scored {student.GPA}")
# a


count1 = int(input("How many students?"))
for i in range(count1):
    print("The student number", i + 1, "information:")
    add_student_info(c1ass)

count2 = int(input("How many courses?"))
for i in range(count2):
    print("The course number", i + 1, "info:")
    add_course_info(courses)

