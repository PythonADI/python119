def add(x, y):
    return x + y


def find(arr, n):
    """
    find and return index of n
    incase n is not in arr return -1
    """
    for i, elem in enumerate(arr):
        if elem == n:
            return i

    return -1





print(add(7, 5))
print(add(7, add(2, 9)))

nums = [-7, 8, 10, -11, 2, 4]
x = 9
print(f'{find([1, 2, 3, 4], 7) = }')
print(f'{find([1, 2, 3, 4], 2) = }')
print(f'{find(nums, 2) = }')
print(f'{find(nums, 7) = }')
print(f'{find(nums, x) = }')

