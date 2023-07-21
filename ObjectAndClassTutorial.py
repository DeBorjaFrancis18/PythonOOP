class Character:
    name = "Name"
    hp = 100
    mp = 50
    atk = 12
    lvl = 1

charOne = Character()
charTwo = Character()

charOne.name = "Francis"
charOne.mp = 100
print(f"Character One: {charOne.name}")
print(f"HP: {charOne.hp}")
print(f"MP: {charOne.mp}")

charTwo.name = "Andrea"
print(f"Character Two: {charTwo.name}")
print(f"HP: {charTwo.hp}")
print(f"MP: {charTwo.mp}")
print("\n")
class Product:
    ID = 1000
    name = "name"
    qty = 0

productOne = Product()
productOne.name = "milk"
productOne.ID = 1001
productOne.qty = 99

print(productOne.name)
print(productOne.ID)
print(productOne.qty)
