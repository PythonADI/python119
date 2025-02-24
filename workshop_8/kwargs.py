def print_details(a, b, *args, something, **kwargs):
    print(f"{a = }, {b = }, {args = }, {something = }, {kwargs = }")


print_details(6, 78, 4, 5, 7, 8, 9, 3, 2, something=17, test=17, first_name="George")

print(5, 7, 8, 9, sep=" | ", end="\n")
print("This is another print")