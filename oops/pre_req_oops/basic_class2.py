# Class of a Person -> name,age,gender
# Intro -> My name is {name}, gender is {gender}, age is {age}

class person:
    # FIELDS / Variable
    # Constructor -> used to initialize the objects
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age 
        self.gender = gender
    

    # METHODS
    def displayInfo(self):
        print("------------------------------------------------")
        print("Person Info")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")


# Object of a Person Class

p1 = person("Rohit Sharma",30,"Male") # Python internally calls __init__()
p2 = person("Rohini Gupta",25,"Female")


p1.displayInfo()
p2.displayInfo()
