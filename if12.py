'''
WAP to accept marks of 5 subject
Display sum and average
Based on average display grades:
if avg is above 90 -> A
if avg is above 75 -> B
if avg is above 50 -> C
if avg is above 35 -> D
if avg below 35 -> Fail
'''

m1 = int(input("Enter subject 1:"))
m2 = int(input("Enter subject 2:"))
m3 = int(input("Enter subject 3:"))
m4 = int(input("Enter subject 4:"))
m5 = int(input("Enter subject 5:"))

sum = m1+m2+m3+m4+m5 
avg = sum / 5

print(f"Total Marks= {sum}")
print(f"Average Marks = {avg}")
# Check all marks are greater than 35
if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    if avg >= 90:
        print("A")
    elif avg >= 75:
        print("B")
    elif avg >= 50:
        print("C")
    else:
        print("D")
else:
    print("Fail")
