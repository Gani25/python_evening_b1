# WAP to print sum of 1 to n

# 1 + 2 + 3 + 4 + 5 + .... n = based on n
# start = 1, stop = n, step = 1

i = 1
sum = 0
n = int(input("Enter a number: "))

while i <= n:

    sum = sum + i 

    i = i + 1

print(f"The sum of 1 to {n} is {sum}")