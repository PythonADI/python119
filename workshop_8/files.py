"""
- r - read (default)
- a - append (creates new file or append to the end for existing one)
- w - write (creates new file or overwrites existing one)
"""

# f = open("./workshop_8/test.txt")

# # print(f.read())

with open("./workshop_8/test.txt") as f:
    for line in f.readlines():
        print(line, end="")


# f.close()

name = input("Enter your name: ")
file_name = input("File: ")
with open(f"./workshop_8/{file_name}", "a") as f:
    # print(f.read())
    f.write(f"This is a new {name}\n")
    f.write("With a new paragraph\n")
    f.write("3rd line\n")
