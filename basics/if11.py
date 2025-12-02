# WAP to print FIZZBUZZ based on below criteria:
# FIZZ -> If number is divisible by 3
# BUZZ -> If number is divisible by 5
# FIZZBUZZ -> If number is divisible by 3 as well as 5
# number -> If number is not divisible by 3 as well as 5

# input = 1
# conditions = 4 (if elif elif else)
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FIZZBUZZ")
elif num % 5 == 0:
    print("BUZZ")
elif num % 3 == 0: 
    print("FIZZ")
else:
    print(num)