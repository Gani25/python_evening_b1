# Patterns 1

n = int(input("Enter a number: "))

# ROW
i = 1

while i <= n:

    # COLUMN
    j = 1
    while j <= i:
        print("* ",end="")
        j = j + 1

    i = i + 1
    print()