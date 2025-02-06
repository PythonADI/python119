# ask user to enter number, if user does not give us a number ask again
# ensure you get the number from user no matter what

n = input("Enter a number: ")
while not n.isdigit():
    if n == "q":
        print("Bye")
        quit()
    print("Please enter correct number")
    n = input("Enter a number: ")

n = int(n)
print(type(n), n)
