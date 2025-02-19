class Student:
    Id: int
    Name: str
    DoB: str
    courses: []

    def __init__(self, id, name, dob):
        self.Id = id
        self.Name = name
        self.DoB = dob
        self.courses = []

    def getId(self):
        return int(self.Id)

    def getName(self):
        return str(self.Name)

    def getDoB(self):
        return str(self.DoB)

    def getMark(self):
        for mark in self.courses:
            print(f"Course: {mark.Course}")
            print(f"Mark: {mark.Mark}")

    def toString(self):
        print(f"Id: {self.getId()}")
        print(f"Name: {self.getName()}")
        print(f"Courses: {len(self.courses)}")


class Course:
    Id: int
    Name: str
    c1ass: []

    def __init__(self, id, name):
        self.Id = id
        self.Name = name
        self.c1ass = []

    def setId(self, id):
        self.Id = id

    def setName(self, name):
        self.Name = name

    def getId(self):
        return self.Id

    def getName(self):
        return self.Name

    def getMark(self):
        for mark in self.c1ass:
            print(f"Student: {mark.Student}")
            print(f"Mark: {mark.Mark}")

    def toString(self):
        print(f"Id: {self.getId()}")
        print(f"Name: {self.getName()}")
        print(f"Number of students: {len(self.c1ass)}")


class Mark:
    Course: str
    Student: str
    Mark: float

    def __init__(self, Course, Student):
        self.Course = Course
        self.Student = Student
        self.Mark = -1.0

    def setCourse(self, course):
        self.Course = course

    def setStudent(self, student):
        self.Student = student

    def setMark(self, mark):
        self.Mark = mark

    def getCourse(self):
        return self.Course

    def getStudent(self):
        return self.Student

    def getMark(self):
        return self.Mark

    def display4Course(self):
        print(f"Student: {self.Student}")
        print(f"Mark: {self.Mark}")


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


def add_course_info(courses):
    print("Enter course info")
    id = int(input("ID:"))
    name = str(input("Name:"))
    course = Course(id, name)
    courses.append(course)
    print("This course is added")


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
        student.Mark = mark


def display_marks(c1ass, courses):
    for c in courses:
        print(f"In course number {courses[c-1]}:")
        for student in c1ass:
            print(f"Student {student.name} has scored {student.Mark}")
# a


count1 = int(input("How many students?"))
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
    5. Make a student learn
    6. Mark a student
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
        else:
            print("Try again")


student_management()
