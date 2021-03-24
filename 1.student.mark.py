def studentcount():
    count= int(input("How many?"))
    return count

def inputstudentinfo():
    print("Enter student info:")
    id = input("- ID")
    name=
    dob=
    student ={ "id": id, "name": name, "dob": dob}
    return student

count = studentcout()
students = []
for i in range (0, count):
    s = inputstudentinfo()
    students += [s]
