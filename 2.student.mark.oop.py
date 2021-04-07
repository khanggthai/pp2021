class Student:
    Id: int
    Name: str
    DoB: str
    CoursesList: []


Student = {
    "Id": "",
    "Name": "",
    "DoB": ""
}
Course = {
    "Id": "",
    "Name": "",
    "Mark": []
}
Mark = {
    "Name": "",
    "Mark": -1.0
}
c1ass = []
courses = []


def addstudentinfo(c1ass):
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


def addcourseinfo(courses):
    print("Enter course info")
    id = input("ID:")
    Course.update({"Id": id})
    name = input("Name:")
    Course.update({"Name": name})
    course_copy = Course.copy()
    courses.append(course_copy)
    print("This course is added")


def displaystudent(c1ass):
    print(f"There are {len(c1ass)} students.")
    for i in c1ass:
        print(i.get("Id") + " : " + i.get("Name"))


def displaycourses(courses):
    print(f"There are {len(courses)} courses.")
    for s in courses:
        print(s.get("Id") + " : " + s.get("Name"))


def enrollcourse(c1ass, courses):
    print("Which course are they enrolling for?")
    displaycourses(courses)

    not_found_course = True
    courseId = (str)(input())
    while not_found_course:
        for c in courses:
            if c.get("Id") == courseId:
                not_found_course = False
                break
        if (not_found_course):
            print("Course not found! Try another one?")
            n = input()

    print("Who will enroll in this course")
    print("0 : No one.")
    displaystudent(c1ass)

    studentId = (str)(input())
    while studentId != 0:
        for s in c1ass:
            if s.get("Id") == studentId:
                Mark.update({"Name": s.get("Name")})
                ["Mark"].append(Mark)
        print("Who else will enroll in this course")
        print("0 : No one else.")
        displaystudent(c1ass)
        studentId = (str)(input())


# a

count1 = int(input("How many students"))
for i in range(count1):
    print("The student number", i + 1, "information:")
    addstudentinfo(c1ass)

count2 = int(input("How many courses?"))
for i in range(count2):
    print("The course number", i + 1, "info:")
    addcourseinfo(courses)


def options():
    print("""Choose?
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
            addstudentinfo(c1ass)
        elif option == 2:
            addcourseinfo(courses)
        elif option == 3:
            displaystudent(c1ass)
        elif option == 4:
            displaycourses(courses)
        elif option == 5:
            enrollcourse(c1ass, courses)
        else:
            print("Try again")


student_management()