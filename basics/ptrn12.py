n = int(input("Enter a number: "))


i = 1
# ROW
while i <= n:

    # SPACE
    sp = 1
    while sp <= n - i:
        print("  ",end="")
        sp = sp + 1
    
    # STAR j
    j = 1
    while j <= 2 * i - 1:
        print("* ",end="")
        j = j + 1

    # NEWLINE
    print()
    i = i + 1