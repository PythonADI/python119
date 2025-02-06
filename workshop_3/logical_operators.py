temp = 31


# if temp < 9 and temp > -5:
#     print("it is cold")

# -5 < temp and temp < 9
if -5 < temp < 9:
    print("it's chilly")
elif -40 < temp <= -5:
    print("It's freezing")
elif temp < -40:
    print("I'm dying")
else:
    print("It's warm")


if temp < -30 or 30 < temp:
    print("I don't like this temperature")
else:
    print("I love this kind of temperature")


if not temp < 30:
    print("it's greater than 30")
