# WAP to check whether the number is even or odd.
# Even number -> Divide the number by 2 and if remainder is 0
# Odd number -> Divide the number by 2 and if remainder is non 0

# Input = 1, conditions = 2

n = int(input("Enter a number: "))

remainder = n % 2
if remainder == 0:
    print(f"Number = {n} is even number")
else:
    print(f"Number = {n} is odd number")

# TASKS
# 1. WAP to check whether the user is eligible for license or not by accepting age

# 2. WAP to check whether the number is divisible by 5 or not

# 3. WAP to check whether the last digit of number is divisible by 3 or not
# Example -> n = 189, last_digit = 9  