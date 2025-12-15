# Class of a Person -> name,age,gender
# Intro -> My name is {name}, gender is {gender}, age is {age}

class person:
    # FIELDS / Variable
    name = "SPRK"
    gender="Male"
    age = 40

    # METHODS
    def displayInfo(self):
        print("------------------------------------------------")
        print("Person Info")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")


# Object of a Person Class

p1 = person()
p2 = person()

p1.name = "Saurabh Sharma"
p1.age = 20

p2.name = "Saieli Gupta"
p2.age = 25
p2.gender = "Female"

p1.displayInfo()
p2.displayInfo()