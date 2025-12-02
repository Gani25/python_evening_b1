# Pascal Traingle

n = int(input("Enter a number: "))

i = 1

while i <= n:

    sp = 1
    while sp <= n-i:
        print(" ", end="")
        sp = sp + 1

    j = 1
    passcal_number = 1
    while j <= i:
        print(f"{passcal_number} ",end="")
        #Formula to calculate pascalnumber
        passcal_number = passcal_number * (i-j) // j
        j = j + 1
    i = i+1
    print()