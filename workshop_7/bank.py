"""
Program for bank account management

Functionality:
1. user registration (name, generate unique id [number], balance)
2. transfer (from one account to another)
3. Deposit
4. Withdraw
"""
import math

users = []

def save_user(id_, name, initial_balance):
    users.append({
        "id": id_,
        "name": name,
        "balance": initial_balance
    })


def get_number(text, min_ = -math.inf, max_ = math.inf):
    while True:
        print(text)
        user_input = input(">>> ")

        try:
            number = int(user_input)
        except ValueError:
            print("Please Enter Correct number format!")
            continue

        if number < min_ or max_ < number:
            print(f"Plase Enter number in range [{min_}, {max_}]")
            continue

        return number


def register_user():
    name = input("Enter Name: ")
    id_ = len(users)
    balance = get_number("Enter Inital Deposit:", 0)
    print(f"Sucessfully registered user {name} ID: {id_}")
    save_user(id_, name, balance)


def print_all_available_users():
    for user in users:
        print(f"{user['id']} | {user['name']} | {user['balance']}")


def change_balance(user, amount):
    if user["balance"] + amount < 0:
        print(f"No funds available; available balance {user['balance']}")
        return False
    user["balance"] += amount
    print(f"Successful operation. New balance: {user['balance']}$")
    return True


def find_user(id_):
    for user in users:
        if user['id'] == id_:
            return user
    return None


def find_user_and_withdraw():
    id_ = get_number("Enter ID:", 0)
    user = find_user(id_)
    print(f"Found user: {user['name']}")
    amount = get_number("Enter amount:", 0)
    print(f"Withdrawing {amount}$ to user: {user['id']}")
    change_balance(user, -amount)


def find_user_and_deposit():
    id_ = get_number("Enter ID:", 0)
    user = find_user(id_)
    if user is None:
        print("User does not exist!")

    print(f"Found user: {user['name']}")
    amount = get_number("Enter amount:", 0)
    print(f"Depositing {amount}$ to user: {user['id']}")
    change_balance(user, amount)


def transfer():
    from_user = find_user(get_number("Enter ID:", 0))
    if from_user is None:
        print("User does not exist!")
        return

    to_user = find_user(get_number("Enter ID:", 0))
    if to_user is None:
        print("User does not exist!")
        return

    amount = get_number("Enter amount:", 0)

    if change_balance(from_user, -amount):
        change_balance(to_user, amount)


def main():
    while True:
        print("\n", "-" * 10, "\n", sep="")
        command = input("Enter Command: ")
        if command == "add":
            register_user()
        elif command == "list":
            print_all_available_users()
        elif command == "deposit":
            find_user_and_deposit()
        elif command == "withdraw":
            find_user_and_withdraw()
        elif command == "transfer":
            transfer()
        else:
            print("Uknown Command, plase try something else!")


main()
