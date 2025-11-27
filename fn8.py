# Function Callstack

def addition(n1,n2):

    sum = n1+n2

    print(f"{n1} + {n2} = {sum}")

    # calling subtraction
    subtraction(n1,n2)

def subtraction(n1,n2):

    multiplication(n1,n2)

    subt = n1-n2

    print(f"{n1} - {n2} = {subt}")


def multiplication(a,b):
    mul = a*b

    print(f"{a} * {b} = {mul}")


num1 = 10
num2 = 6
addition(num1, num2)









