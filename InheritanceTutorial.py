#PARENT CLASS
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def introduce(self):
        print(f"Hi I am {self.firstName} {self.lastName}")

#CHILD CLASS
class Student(Person):
    pass

class Override(Person):
    def __init__(self, firstName, lastName, talent):
        super().__init__(firstName, lastName)
        self.talent = talent

    def introduce(self):
        super().introduce()
        print("I am override")

    def sayTalent(self): #ADDING FUNCTION
        print(f"My talent is {self.talent}")

pOne = Person("Francis", "De Borja") #Parent Objec
pOne.introduce()
print()
sOne = Student("Andrea", "Esguerra") #Child Object
sOne.introduce()
print()
overOne = Override("Carl", "Lat", "Dancing") #Overriding Object
overOne.introduce()
overOne.sayTalent()

class Employee(Person):
    def __init__(self, firstName, lastName, salary):
        super().__init__(firstName, lastName)
        self.salary = salary

    def introduce(self):
        super().introduce()

    def saySalary(self):
        print(f"My salary is {self.salary}")

print("\nNew Employee")
eOne = Employee("Noaim", "Abubacar", 30000)
eOne.introduce()
eOne.saySalary()