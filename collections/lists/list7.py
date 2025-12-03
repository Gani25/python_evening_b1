nums = [10,20,30,60,80]


newList = nums 

print("Old Nums:",nums)
print("New List:",newList)

newList.insert(2,600)

print("After insert")
print("Old Nums:",nums)
print("New List:",newList)

newCopyList = nums.copy()
print("Old Nums:",nums)
print("New Copy Nums:",newCopyList)

newCopyList.insert(1,"SPRK Tech")

print("After insert on copy nums")
print("Old Nums:",nums)
print("New Copy Nums:",newCopyList)