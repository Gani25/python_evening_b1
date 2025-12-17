class person:

    def __init__(self, name, age):

        if(age < 0 or age > 120):
            raise Exception("Age cannot be negative or greater then 120")
        
        self.name=name
        self.age=age

    
    def __str__(self):
        return f"Name = {self.name}\nAge = {self.age}"


if(__name__ == "__main__"):

    try:
        p1 = person("Ashish Verma",-5)

        print(p1)
    except Exception as e:
        print(e)
        