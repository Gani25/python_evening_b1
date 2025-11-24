n = int(input("Enter a number: "))

# row
i = 1

while i <= n:

    #Left Star Triangle
    j = 1
    while j <= i:
        print("* ",end="")
        j = j + 1
    
    sp = 1
    while sp <= (2 * (n-i) - 1):
        print("  ",end="")
        sp = sp + 1
    
    #Right Star Triangle
    j = 1
    while j <= i:
        if j < n:
            print("* ",end="")
        j = j + 1
    #NewLine
    print()
    i = i + 1 

# LOWER HALF
# row
i = n - 1

while i >= 1:

    #Left Star Triangle
    j = 1
    while j <= i:
        print("* ",end="")
        j = j + 1
    
    sp = 1
    while sp <= (2 * (n-i) - 1):
        print("  ",end="")
        sp = sp + 1
    
    #Right Star Triangle
    j = 1
    while j <= i:
        print("* ",end="")
        j = j + 1
    #NewLine
    print()
    i = i - 1 