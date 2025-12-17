try:
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
except ValueError as ve:
    
    print("Invalid n1,n2 =",ve)


try:
    result = n1 / n2
    print(f"{n1} / {n2} = {result}")

except Exception as e:
    print("Result ERROR= ",e)