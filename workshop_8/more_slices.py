import random

nums = []

for i in range(10):
    nums.append(random.randint(-10, 10))

print(f"{nums = }")
n = nums[:]
print(f"{n = }")
print(f"{n == nums = }")
print(f"{n is nums = }")
print(f"{id(n) = }")
print(f"{id(nums) = }")

n.append(7)
print("-" * 10, "After Append", "-" * 10)
print(f"{nums = }")
print(f"{n = }")
print(f"{n == nums = }")
print(f"{n is nums = }")
