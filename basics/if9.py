# WAP to check whether the number is divisible by 3 and 5 both or not
# input = 1
# Conditions = 2

num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"Number = {num} is divisible by both 3 and 5")
else:
    print(f"Number = {num} is not divisible by both 3 and 5")