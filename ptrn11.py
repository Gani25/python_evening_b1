n = int(input("Enter a number: "))

i = 1

#ROW
while i <= n:

    #SPACE
    sp = 1
    while (sp <= n - i):
        print("  ", end="")
        sp = sp + 1

    j = 1
    #COLUMN
    while j <= n:
        print("* ",end="")
        
        j = j + 1
    
    print()
    i = i + 1
    