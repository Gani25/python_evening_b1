# WAP to print first n natural number in reverse order
# start = n , stop = 1, step = -1 
# Example -> n = 6
# 6 5 4 3 2 1  

n = int(input("Enter a number: "))

# start
i = n 

while i >= 1:
    print(i)
    i = i - 1