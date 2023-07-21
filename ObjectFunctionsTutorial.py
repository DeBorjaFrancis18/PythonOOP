class User:
    def __init__(self, fName, lName, likes, friends):
        self.fName = fName
        self.lName = lName
        self.likes = likes
        self.friends = friends

        print(f"{self.fName} is created.")

    def introduce(self):
        print(f"Hi, I am {self.fName} {self.lName}")

    def profile(self):
        print(f"Full Name: {self.fName} {self.lName}")
        print(f"Likes    : {self.likes}")
        print("Friends")
        for i in self.friends:
            print(f"   - {i}")

userOne = User("Francis", "De Borja", 100,
               ["Andrea Esguerra",  "Noaim Abubacar", "Carl Lat"])
userOne.introduce()
userOne.profile()