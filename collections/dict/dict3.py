students =[ {
    "roll_no":101,
    "name":"Shruti Sharma",
    "gender":"Female",
    "marks":[]
},{
    "roll_no":102,
    "name":"Rohini Chavla",
    "gender":"Female",
    "marks":[]
},{
    "roll_no":103,
    "name":"Shubham Kokate",
    "gender":"Male",
    "marks":[]
}
]

print(students)

students[0]["marks"].extend([60,90,85,98,48])
students[0]["percentage"] = sum(students[0]["marks"])/len(students[0]["marks"])

for student in students:
    print("-----------------------------------------------------")
    print("Student Info")
    print("-----------------------------------------------------")
    for key, value in student.items():
        print(f"{key} = {value}")