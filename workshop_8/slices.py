import random

nums = []

for _ in range(20):
    nums.append(random.randint(0, 100))

print(nums, len(nums))
for i in range(10):
    print(nums[i])

print("Last 10 Numbers")
# 90 - 100
for i in range(len(nums) - 10, len(nums)):
    print(nums[i])

# index must be an integer
# print(nums[7.8])
# 100 / 2 - 5, 100 / 2 + 5
print("Middle 10 numbers")
middle_point = len(nums) // 2
for i in range(middle_point - 5, middle_point + 5):
    print(nums[i])


print(nums[:10])
# print(nums[:])
print(nums[-10:])
# print(nums[middle_point - 5:middle_point + 5])

print("Middle 10 numbers with slices")
for num in nums[middle_point - 5:middle_point + 5]:
    print(num)


# print("Evey second number in list")
# for i, num in enumerate(nums):
#     if i % 2 == 1:
#         continue
#     print(num)


print("Evey second number in list")
for num in nums[1::2]:
    print(num)


print(nums[::-1])
