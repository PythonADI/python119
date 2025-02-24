def sum_up(a: int, b: int, *nums: tuple[int]):
    print(f'{nums = }')
    total: int = a + b
    for num in nums:
        total += num

    return total


a = 7
b = 9
print(sum_up(a, b, 9, 11, 31))
