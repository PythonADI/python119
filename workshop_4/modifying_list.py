nums = [1, 2, 3, -4, 5, 6, 7, 8, 9]

nums.append(10)
nums.append(-15)
nums.append(1000)

print(nums)

nums[0] = 999
print(type(len(nums) // 2), len(nums) // 2)
nums[len(nums) // 2] = 27
nums[-1] = -80
print(nums)

nums.pop()
print(nums)
for i in range(7):
    nums.pop()

print(nums)
