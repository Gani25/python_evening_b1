# Dictionary -> word:meaning
# contact book -> name: phone
# password manager -> username: password

# contact book

contacts = {
    "Rohit Sharma":12345678,
    "Rohan Pandey":55668811,
    "Pranjali Shinde":99889988,
    "Rohit Sharma":55668811,
    } 
print(contacts)
print(type(contacts))

contacts["Abdul Gani"] = 12312312
print(contacts)
print(contacts["Rohan Pandey"])
# print(contacts["Shurti Ashtana"]) Error key not exists

contacts.update({"Shoaib Khan":12312345})
print(contacts)
contacts.update({"Abdul Gani":98765432})
print(contacts)
