# WAP to print first n natural numbers
# n -> user will give
# 1 2 3 ..... n

# start = 1, stop = n, step = 1

# initialization
i = 1

# stop -> input
num = int(input("Enter a number: "))

while i <= num:
    print(i, end=" ")
    i = i + 1