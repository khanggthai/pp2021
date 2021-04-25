Student = {
    "Id": int,
    "Name": "",
    "DoB": ""
}
Course = {
    "Id": int,
    "Name": "",
    "Mark": []
}
Mark = {
    "Name": [],
    "Mark": []
}
c1ass = []
courses = []


def add_student_info(c1ass):
    print("Enter student info:")
    id = input("ID: ")
    Student.update({"Id": id})
    name = input("Name:")
    Student.update({"Name": name})
    dob = input("Date of birth:")
    Student.update({"DoB": dob})
    student_copy = Student.copy()
    c1ass.append(student_copy)
    print("This student is added")


def add_course_info(courses):
    print("Enter course info")
    id = input("ID:")
    Course.update({"Id": id})
    name = input("Name:")
    Course.update({"Name": name})
    course_copy = Course.copy()
    courses.append(course_copy)
    print("This course is added")


def display_student(c1ass):
    print(f"There are {len(c1ass)} students.")
    for i in c1ass:
        print(i.get("Id") + " : " + i.get("Name"))


def display_courses(courses):
    print(f"There are {len(courses)} courses.")
    for s in courses:
        print(s.get("Id") + " : " + s.get("Name"))


def mark_student(c1ass, courses):
    print("Which course?")
    display_courses(courses)
    courseId = int(input())
    for c in courses:
        if c.get("Id") == (courseId - 1):
            display_student(c1ass)
            studentId = int(input("Which student?"))
            while studentId != 0:
                for s in c1ass:
                    if s.get("Id") == studentId:
                        Mark.update({"Name": s.get("Name")})
                        ["Mark"].append(Mark)
        else: print("oofs")


# run

count1 = int(input("How many students"))
for i in range(count1):
    print("The student number", i + 1, "information:")
    add_student_info(c1ass)

count2 = int(input("How many courses?"))
for i in range(count2):
    print("The course number", i + 1, "info:")
    add_course_info(courses)


def options():
    print("""
    Choose?
    1. Add a student
    2. Add a course
    3. List students in class
    4. List courses
    5. Mark student in the course
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
            mark_student(c1ass, courses)
        else:
            print("Try again")


student_management()
