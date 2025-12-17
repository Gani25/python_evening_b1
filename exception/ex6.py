# Accept input unless user not give correct value

while True:
    try:
        n1 = int(input("Enter a number: "))

        break
    except Exception as e:
        print(e)
while True:
    try:
        n2 = int(input("Enter a number: "))

        print(f"{n1} / {n2} = {n1/n2}")

        break
    except Exception as e:
        print(e)