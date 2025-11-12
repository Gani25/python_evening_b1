# WAP to print table of n til x iterations

# n = 6, x = 5
# input = 2

# start = 1, stop = iterations(x), step = 1
num = int(input("Enter a number to display table: "))
iteration = int(input("Enter total number of iterations: "))

i = 1

print(f"Table of {num} till {iteration} iterations")
while i <= iteration:

    table = num * i

    print(f"{num} X {i} = {table}")

    i = i + 1

# WAP to print square of 1 to n
# n = 6
# square of 1 is 1
# square of 2 is 4
# square of 3 is 9
# square of 4 is 16
# square of 5 is 25
# square of 6 is 36