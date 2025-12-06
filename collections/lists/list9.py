# 2d list -> List Inside a List

# store infor of student -> rollNo, name, gender -> for 5 students

student1 = [1,"Rohit Raj","Male"]
student2 = [2,"Pranjali Sharma","Female"]
student3 = [3,"Abhishek Gupta","Male"]
student4 = [4,"Ganesh Gaikwad","Male"]
student5 = [5,"Rohini Shinde","Female"]

all_student_mech = [
    [1,"Rohit Raj","Male"],
    [2,"Pranjali Sharma","Female"],
    [3,"Abhishek Gupta","Male"],
    [4,"Ganesh Gaikwad","Male"],
    [5,"Rohini Shinde","Female"]
] 

print(all_student_mech)
print("Last student =",all_student_mech[-1])
print("Second student Name =",all_student_mech[1][1])


for row in all_student_mech:
    print(row)

print("Student Info")
for row in all_student_mech:
    for value in row:
        print(value,end=" ")
    
    print()