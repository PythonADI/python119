import time
import random

heating_on = True
temperature = 26

while True:
    change = random.randint(0, 3)
    if heating_on:
        temperature += change
    else:
        temperature -= change

    print(f"it's {temperature} celsius")
    if temperature < 24:
        print("Turn on heating")
        heating_on = True
    elif temperature > 30:
        print("Turn off heating")
        heating_on = False

    time.sleep(1)
