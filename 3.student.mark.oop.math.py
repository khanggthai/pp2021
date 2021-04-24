import math
import numpy


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

    def setId(self, id):
        self.Id = id

    def setName(self, name):
        self.Name = name

    def setBoB(self, dob):
        self.DoB = dob

    def getId(self):
        return int(self.Id)

    def getName(self):
        return str(self.Name)

    def getDoB(self):
        return str(self.DoB)

    def getMark(self):
        for mark in self.courses:
            print(f"""
                Course: {mark.Course}
                Mark: {mark.Mark}
            """)

    def toString(self):
        print(f"""
    Id: {self.getId()}
    Name: {self.getName()}
    DoB: {self.getDoB()}
    Number of courses: {len(self.courses)}
         """)


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
            print(f"""
                Student: {mark.Student}
                Mark: {mark.Mark}
            """)

    def toString(self):
        print(f"""
    Id: {self.getId()}
    Name: {self.getName()}
    Number of students: {len(self.c1ass)}
        """)


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
        print(f"""
            Student: {self.Student}
            Mark: {self.Mark}
        """)


c1ass = []
courses = []


def addstudentinfo(c1ass):
    print("Enter student info:")
    id = int(input("ID: "))
    name = str(input("Name:"))
    dob = str(input("Date of birth:"))
    student = Student(id, name, dob)
    c1ass.append(student)
    print("This student is added")


def addcourseinfo(courses):
    print("Enter course info")
    id = int(input("ID:"))
    name = str(input("Name:"))
    course = Course(id, name)
    courses.append(course)
    print("This course is added")


def displaystudent(c1ass):
    print(f"There are {len(c1ass)} students.")
    for i in c1ass:
        i.toString()


def displaycourses(courses):
    print(f"The are {len(courses)} courses.")
    for s in courses:
        s.toString()


def searchId(list, id):
    for i in list:
        if i.getId() == id:
            print(i.getName())
            return i


def markcal(student):
    

def enroll():
    displaycourses(courses)
    course = int(input("Which one?"))
    foundCourse = Course(0, "Null")
    foundCourse = searchId(courses, course)
    while not foundCourse:
        course = int(input("Try again? "))
        foundCourse = searchId(courses, course)

    displaystudent(c1ass)
    student = int(input("Which student? "))
    foundStudent = Student(0, "Null", "Null")
    foundStudent = searchId(c1ass, student)
    while not foundStudent:
        student = int(input("Try again? "))
        foundStudent = searchId(c1ass, student)

    mark = Mark(foundCourse, foundStudent)
    foundCourse.c1ass.append(mark)
    foundStudent.courses.append(mark)


def markStudent():
    course = int(input("Which course do you want to give marks? "))
    foundCourse = Course(0, "Null")
    foundCourse = searchId(courses, course)
    while not foundCourse:
        course = int(input("Course not found! Try again? "))
        foundCourse = searchId(courses, course)

    for student in foundCourse.c1ass:
        print(f"Student: {student.Student}")
        mark = float(input("Input mark for this student: "))
        student.Mark = mark


# a

count1 = int(input("How many students are in the class?"))
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
            addstudentinfo(c1ass)
        elif option == 2:
            addcourseinfo(courses)
        elif option == 3:
            displaystudent(c1ass)
        elif option == 4:
            displaycourses(courses)
        elif option == 5:
            enroll()
        elif option == 6:
            markStudent()
        else:
            print("Try again")


student_management()
