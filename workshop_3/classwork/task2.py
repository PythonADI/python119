# ask user for number (n), from 0 to n print out every number that can be divided by 3.5

n = int(input("Enter a number: "))

for x in range(n):
    if x % 3.5 == 0:
        print(x)
