age = input("Enter you are: ")
# print(age.isdigit())

if age.isalpha():
    print("Age cannot be text!")

if age.isdigit():
    # code fragment
    print("Great job")
    age = int(age)
    print(f"You are {age} years old")
    print(f"You will be {age + 1} years old next year")

    if age < 13:
        print("You are a Minor")
    elif age < 20:
        print("you are teenager")
    elif age < 30:
        print("you are young adult")
    elif age < 60:
        print("you are adult")
    else:
        print("You are an elder")

else:
    print("Please enter correct number format!")
