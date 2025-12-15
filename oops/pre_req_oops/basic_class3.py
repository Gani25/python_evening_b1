# Class of a Person -> name,age,gender
# Intro -> My name is {name}, gender is {gender}, age is {age}

class person:
    # FIELDS / Variable
    # Constructor -> used to initialize the objects
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age 
        self.gender = gender
    

    # # METHODS
    # def __str__(self):
    #     return f"------------------------------------------------\nPerson Info\nName = {self.name}\nAge = {self.age}\nGender = {self.gender}"

    # METHODS
    def __str__(self):
        return f"""
------------------------------------------------
Person Info
Name = {self.name}
Age = {self.age}
Gender = {self.gender}
"""


# Object of a Person Class

p1 = person("Rohit Sharma",30,"Male") # Python internally calls __init__()
p2 = person("Rohini Gupta",25,"Female")


print(p1)
print(p2)