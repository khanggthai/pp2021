import math
import numpy
import curses


class Student:
    Id: int
    Name: str
    DoB: str
    GPA: float
    courses: []

    def __init__(self, id, name, dob):
        self.Id = id
        self.Name = name
        self.DoB = dob
        self.GPA = 0
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

    def getGPA(self):
        return float(self.GPA)

    def toString(self):
        print(f"Id: {self.getId()}")
        print(f"Name: {self.getName()}")
        print(f"Courses: {len(self.courses)}")


class Course:
    Id: int
    Name: str
    Credit: int
    c1ass: []

    def __init__(self, id, name):
        self.Id = id
        self.Name = name
        self.c1ass = []

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

    def getCredit(self):
        return self.Credit


class Mark:
    Course: str
    Student: str
    Mark: float
    Credit: int

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

    def getCredit(self):
        return self.Credit

    def display4Course(self):
        print(f"Student: {self.Student}")
        print(f"Mark: {self.Mark}")

