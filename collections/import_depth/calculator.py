def addition(*numbers):
    print(f"Addition of {numbers} = {sum(numbers)}")

def subtraction(n1,n2):
    print(f"{n1} - {n2} = {n1-n2}")

def power(a,b):
    print(f"{a} raise to {b} = {a**b}")


# I only want to execute this block of code when current file runs 
# Don't want to run when execute through imports

# print(__name__)
if(__name__ == "__main__"):
    power(5,3)
    addition(6,10)
    subtraction(15,3)