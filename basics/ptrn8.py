n = int(input("Enter a number: "))

# ROW
i = n
while i >= 1:
    #SPACES
    sp = 1
    while sp <= n-i:
        print("  ", end="")
        sp = sp + 1

    # COLUMN
    j = 1
    while j <= i:
        print("* ",end="")
        j = j + 1
    
    # NEW LINE
    print()
    i = i - 1