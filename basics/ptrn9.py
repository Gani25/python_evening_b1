n = int(input("Enter a number: "))

# ROW
i = 1
while i <= n:
    

    # COLUMN
    j = 1
    while j <= n:
        if(i == j or (i + j) == (n + 1)):
            print("* ",end="")
        else:
            print("  ",end="")
        j = j + 1
    
    # NEW LINE
    print()
    i = i + 1