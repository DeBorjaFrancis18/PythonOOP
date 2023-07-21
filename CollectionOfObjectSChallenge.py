class Student:
    def __init__(self, name, course, year, section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def profile(self):
        print(f"Name    : {self.name}")
        print(f"Course  : {self.course}")
        print(f"Year    : {self.year}")
        print(f"Section : {self.section}")

listOfStudents = []
add = True
while add == True:
    print()
    name = input("Name    : ")
    course = input("Course  : ")
    year = input("Year    : ")
    section = input("Section : ")
    s = Student(name, course, year, section)
    listOfStudents.append(s)
    print()
    choice = input("Add Another Student? [Y/Any Char] : ")
    if choice == "Y" or choice == 'y': pass
    else:
        add = False
        print("Student profile creation complete.")

print()
for i in range(len(listOfStudents)):
    print(f"Student #{i+1}")
    listOfStudents[i].profile()
    print()