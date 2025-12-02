# WAP to check greatest of 2 numbers or both are equal
# input = 2
# conditions = 3

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

if n1 > n2:
    print(f"Number 1 = {n1} is greater than Number 2 = {n2}")
    # print("Number 1 =",n1,"is greater than Number 2 =",n2)
elif n2 > n1:
    print(f"Number 2 = {n2} is greater than Number 1 = {n1}")
else:
    print(f"Both number = {n1} are equal")