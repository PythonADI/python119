def add(a, b = -100):
    print(f"{a = }, {b = }")


# positional argument
add(5, 7)
add(7, 5)
# keyword argument
add(a=7, b=5)
add(b=7, a=5)

add(8, b=2)
# positional arguments should always be written
# add(a=8, 2)


add(8)
add(a=-11)
