# Function returning multiple values

def calculation(n1:int, n2:int):

    add= n1+n2
    subt= n1-n2
    multi= n1*n2
    power= n1**n2
    divide= n1/n2
    brand = "Casio"

    return add,subt,multi,power,divide,brand


n1 = 20
n2 = 3
results = calculation(n1,n2)

print(f"Calculation Result of n1 = {n1}, n2 = {n2}, results = {results}")

print(f"Brand: {results[-1]}")
print(f"Addition of {n1}, {n2} = {results[0]}")
print(f"Subtraction of {n1}, {n2} = {results[1]}")
print(f"Multiplication of {n1}, {n2} = {results[2]}")
print(f"Power of {n1}, {n2} = {results[3]}")
print(f"Division of {n1}, {n2} = {results[4]}")

n1 = 15
n2 = 5

addition, subtraction, multiplication, power, division, brand = calculation(n1,n2)
print(f"Brand: {brand}")
print(f"Addition of {n1}, {n2} = {addition}")
print(f"Subtraction of {n1}, {n2} = {subtraction}")
print(f"Multiplication of {n1}, {n2} = {multiplication}")
print(f"Power of {n1}, {n2} = {power}")
print(f"Division of {n1}, {n2} = {division}")