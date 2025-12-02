# Patterns 1

n = int(input("Enter a number: "))

# ROW
i = 1 # START

while i <= n:

    #COLUMN
    j = 1 # column Start

    while j <= n:

        # conditions
        if (i + j) % 2 == 0:
            print("0 ", end="")
        else:
            print("1 ", end="")

        j = j + 1

    #Increase ROW
    i = i + 1
    print()