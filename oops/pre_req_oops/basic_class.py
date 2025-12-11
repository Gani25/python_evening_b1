# Class of a Person -> name,age,gender
# Intro -> My name is {name}, gender is {gender}, age is {age}

class person:
    # FIELDS / Variable
    name = "SPRK"
    gender="Male"
    age = 40


# Object of a Person Class

p1 = person()
p2 = person()

print(type(p1))
print(p1)
print(p2)

print("------------------------------------------------")
print("Person Info of P1")
print(f"Name = {p1.name}")
print(f"Age = {p1.age}")
print(f"Gender = {p1.gender}")
print("------------------------------------------------")
print("Person Info of P2")
print(f"Name = {p2.name}")
print(f"Age = {p2.age}")
print(f"Gender = {p2.gender}")

p1.name = "Saurabh Sharma"
p1.age = 20
print("------------------------------------------------")
print("Person Info of P1")
print(f"Name = {p1.name}")
print(f"Age = {p1.age}")
print(f"Gender = {p1.gender}")

p2.name = "Saieli Gupta"
p2.age = 25
p2.gender = "Female"
print("------------------------------------------------")
print("Person Info of P2")
print(f"Name = {p2.name}")
print(f"Age = {p2.age}")
print(f"Gender = {p2.gender}")