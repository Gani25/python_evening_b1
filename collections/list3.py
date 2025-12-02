nums = []

print("My List =", nums)

nums.append(50)
nums.append(10)
print("My List =", nums)

nums.extend([60,80,90])
print("My List =", nums)

nums.insert(1,-55)
nums.insert(-3,-55)
nums.append(-55)
nums.append(-55)
print("My List =", nums)

print(f"Deleted element at last index = {nums.pop()}")
print("My List =", nums)
print(f"Deleted element at index 1 = {nums.pop(1)}")
print("My List =", nums)

nums.remove(-55)
print("My List deleted -55 as a value = ", nums)