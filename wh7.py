# WAP to print square of 1 to n
# n = 6
# square of 1 is 1
# square of 2 is 4
# square of 3 is 9
# square of 4 is 16
# square of 5 is 25
# square of 6 is 36

i = 1
n = int(input("Enter a number: "))
while i <= n:
    # square = i * i
    square = i ** 2
    print(f"The square of {i} is {square}")
    i = i + 1

# WAP to print first n natural number in reverse order
# start = n , stop = 1, step = -1 
# Example -> n = 6
# 6 5 4 3 2 1  