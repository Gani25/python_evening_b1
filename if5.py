# 3. WAP to check whether the last digit of number is divisible by 3 or not
# Example -> n = 189, last_digit = 9  

#Input = 1
# Conditions = 2

number = int(input("Enter a number: "))

last_digit = number % 10

remainder_by_3 = last_digit % 3

if remainder_by_3 == 0:
    print(f"Number = {number}, last digit = {last_digit} is divisible by 3")
else:
    print(f"Number = {number}, last digit = {last_digit} is not divisible by 3")