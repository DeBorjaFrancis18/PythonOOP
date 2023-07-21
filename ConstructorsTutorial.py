class Character:
    def __init__(self, name, hp, mp, atk, lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk =atk
        self.lvl = lvl
        print("Created " + self.name)


charOne = Character("Francis", 100, 100, 10, 1)
charTwo = Character("Andrea", 100, 50, 5, 1)
print(charOne.name)
