n = int(input("Enter a number: "))

i = 1

#ROW
while i <= n:

    j = 1
    #COLUMN
    while j <= n:
        if i == 1 or i == n or j == 1 or j == n:
            print("* ",end="")
        else:
            print("  ",end="")
        j = j + 1
    
    print()
    i = i + 1
    