try:
    num1 = int(input(">>> "))
    num2 = int(input(">>> "))
except ValueError:
    print("Please user correct number format!")

# raise ValueError("This is a value error")

try:
    result = num1 / num2
    print(f"{result = }")
    # raise FileNotFoundError()
except ZeroDivisionError as e:
    print(e)
    print("number should not be 0")
except NameError:
    print("Please use correct numbers!")
except Exception as e:
    print(e, type(e))
    print("Unexpected Error :( [Please contact developer]")
