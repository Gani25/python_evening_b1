# WAP to find factorial of n using recursion(fn with return type)

def calculate_factorial(number:int):

    if number < 0:
        return -1
    if number == 0 or number == 1:
        return 1

    return number * calculate_factorial(number - 1)


num = int(input("Enter a number: "))
result = calculate_factorial(number=num)
if (result == -1):
    print("Number cannot be negative..")
else:
    print(f"Factorial of {num} = {result}")

# WAP to print sum of n natural number using recurssion
# n = 10.. 10 + call(9)
                # 9 + call(8)