# 2. WAP to check whether the number is divisible by 5 or not
#Input = 1
# Conditions = 2

number = int(input("Enter a number: "))

if number % 5 == 0:
    print(f"Number = {number} is divisible by 5")
else:
    print(f"Number = {number} is not divisible by 5")

'''
remainder_by_5 = number % 5

if remainder_by_5 == 0:
    print(f"Number = {number} is divisible by 5")
else:
    print(f"Number = {number} is not divisible by 5")
'''