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
    def __str__(self):
        return f"------------------------------------------------\nPerson Info\nName = {self.name}\nAge = {self.age}\nGender = {self.gender}"

    
    def __gt__(self,other):
        
        return self.age > other.age
    
    def __ge__(self,other):
        
        return self.age >= other.age


    
# Object of a Person Class

p1 = person("Rohit Sharma",30,"Male") # Python internally calls __init__()
p2 = person("Rohini Gupta",30,"Female")
p3 = person("Rohini Gupta",20,"Female")


print(f"Is p1 greater than p2: age? {p1>=p2}")
print(f"Is p1 greater than p3: age? {p1>p3}")