student1 = {
    "roll_no":101,
    "name":"Shruti Sharma",
    "gender":"Female",
    "marks":[]
}

# print(student1)

print("-------------------------------------------------")
print("Student Info")
print("-------------------------------------------------")
for key in student1.keys():
    print(f"{key} = {student1[key]}")
    # print(f"{key} = {student1.get(key)}")

print("-------------------------------------------------")
print("Student Info")
print("-------------------------------------------------")
for k,v in student1.items():
    print(k,"=",v)

print(type(student1["marks"]))

student1["marks"].append(55)
student1["marks"].extend([60,90,85,95])

print("-------------------------------------------------")
print("Student Info")
print("-------------------------------------------------")
for k,v in student1.items():
    print(k,"=",v)

student1["percentage"] = sum(student1["marks"])/len(student1["marks"])

print("-------------------------------------------------")
print("Student Info")
print("-------------------------------------------------")
for k,v in student1.items():
    print(k,"=",v)