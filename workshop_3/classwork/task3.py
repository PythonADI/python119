# ask user for 3 numbers (s, e, f) print every number from s to e that is divisible by (f / 2)

s = int(input("s: "))
e = int(input("e: "))
f = int(input("f: "))

for x in range(s, e):
    if x % (f / 2) == 0:
        print(x)
