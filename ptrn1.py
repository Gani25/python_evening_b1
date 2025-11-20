# Patterns 1

n = int(input("Enter a number: "))

# ROW
i = 1 # START

while i <= n:

    #COLUMN
    j = 1 # column Start

    while j <= n:

        print("* ",end="")

        j = j + 1

    #Increase ROW
    i = i + 1
    print()