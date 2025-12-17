class person:

    def __init__(self, name, age):

        if(age < 0 or age > 120):
            raise AgeInvalidError("Age cannot be negative or greater then 120")
        
        self.name=name
        self.age=age

    
    def __str__(self):
        return f"Name = {self.name}\nAge = {self.age}"

class AgeInvalidError(Exception):

    def __init__(self, *args):
        super().__init__(*args)


if(__name__ == "__main__"):
    try:
        p1 = person("Ashish Verma",-5)

        print(p1)
    except AgeInvalidError as ae:
        print(ae)
        