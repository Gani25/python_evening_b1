nums = set()

print(nums)
print(type(nums))

nums.add(50)
nums.add(100)
nums.add(-5)
nums.add(25)
nums.add("Tech")
nums.add(50)
nums.add(100)
nums.add(50)
nums.add("SPRK")
print(nums)

nums.update({60,80,50,1})

print(nums)
nums.discard(1000)
print(nums)
nums.discard(100)
print(nums)
print(nums.pop())

print(nums)
print(nums.pop())
print(nums)
