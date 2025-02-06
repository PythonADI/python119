temperatures = [-5, 7, -1, 3, 2, 9, 17, 20, 19]

print(f"We recorded total of {len(temperatures)} temperatures")
# print(temperatures)
print(f"Day 1 temperature was: {temperatures[0]}")
# print(f"Last Day temperature was: {temperatures[len(temperatures) - 1]}")
print(f"Last Day temperature was: {temperatures[-1]}")


for i in range(len(temperatures)):
    print(f"Day {i + 1} tempreatures was: {temperatures[i]}")


print("Directly in operator on list")
for temperature in temperatures:
    print(temperature)

print("Directly in operator on list (enumerate)")
for i, temperature in enumerate(temperatures):
    print(f"Day {i + 1} temperature was {temperature}")
