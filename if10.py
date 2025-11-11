# WAP to check whether the triangle is isoceles,equilateral, scalene
# Isoceles = Any 2 sides are equal
# equilateral = All sides are equal
# Scalene = No sides are equal

# Input = 3
# Condition = 3 (if elif else)

s1 = int(input("Enter side 1: "))
s2 = int(input("Enter side 2: "))
s3 = int(input("Enter side 3: "))

if s1 > 0 and s2 > 0 and s3 > 0:
    if s1 == s2 and s2 == s3:
        print("Equilateral Triangle")

    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Isoceles Triangle")

    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")