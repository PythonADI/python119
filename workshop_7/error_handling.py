try:
    num = int(input("Enter number (1): "))
    num2 = int(input("Enter number (2): "))
except ValueError:
    print("Please enter correct number")
    quit()

try:
    print(num / num2)
except ZeroDivisionError:
    print("Divisor (number 2) should not be 0")
    quit()

print(num, type(num))
print("Done")