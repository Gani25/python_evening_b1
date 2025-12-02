# Perfect Number

num = int(input("Enter a number: "))

i = 1
sum = 0

while (i <= num - 1):

    if num % i == 0:
        # divisor
        sum = sum + i
    i = i + 1

if sum == num:
    print(f"Number = {num} is a perfect number")
else:
    print(f"Number = {num} is not a perfect number, Sum of divisor = {sum}")

