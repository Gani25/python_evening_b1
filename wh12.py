# WAP to print sum of digits of n

# n = 189 
# 9 + 8 + 1 = 18

# n = 1221 
# 1 + 2 + 2 + 1  = 6

n = int(input("Enter a number: "))
sum = 0
# copy store
i = n  # start
while i > 0:
    last_digit = i % 10
    sum = sum + last_digit

    i = i // 10

print(f"The sum of digit of {n} = {sum}")

# WAP to reverse a number
# n = 1352 -> reverse = 2531 