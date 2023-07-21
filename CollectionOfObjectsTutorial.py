class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def introduce(self):
        print(f"I am {self.name}")

people = []
for i in range(3):
    name = input(f"Enter Name {i+1}: ")
    p = Person(name)
    people.append(p)
print()
for i in range(len(people)): #reading using ForLoop
    print (f"Name {i+1}: {people[i].name}")
    people[i].introduce()
    print()