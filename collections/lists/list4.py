nums = []

print("My List =", nums)

nums.append(50)
nums.append(10)
print("My List =", nums)

nums.extend([60,80,90])
print("My List =", nums)

nums.append(20)
nums.insert(0,-55)
nums.insert(-3,-55)
nums.append(-55)
nums.append(-55)

nums.append(20)

nums.append(33)
nums.append(24)
nums.append(20)
print("My List =", nums)

print(f"-55 at index numbers = {nums.index(-55)}")
print("My List =", nums)
print(f"1st occurence of 20 at index numbers = {nums.index(20)}")
print("My List =", nums)
print(f"2nd occurence of 20 at index numbers = {nums.index(20, nums.index(20)+1 )}")
print("My List =", nums)
print(f"3rd occurence of 20 at index numbers = {nums.index(20, nums.index(20, nums.index(20)+1)+1 )}")
print("My List =", nums)

# Delete 2nd occurence of 20

print(f"Deleting 2nd occ of 20 = {nums.pop(nums.index(20, nums.index(20)+1 ))} ")
print("My List =", nums)