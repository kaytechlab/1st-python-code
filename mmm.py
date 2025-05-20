accounts = {
    "kay": 1000000,
    "Daniel": 2000000
}
accounts = {}

def deposit():
    name = input("Enter account name to deposit into: ")
    amount = int(input("Enter amount to deposit: "))
    accounts[name] = accounts.get(name, 0) + amount
    print(f"{amount} deposited into {name}'s account.")

def check_balance():
    name = input("Enter account name to check balance: ")
    if name in accounts:
        print(f"{name}'s balance is {accounts[name]}")
    else:
        print("ERROR: Account does not exist.")

def transfer():
    sender = input("Enter sender's name: ")
    receiver = input("Enter receiver's name: ")
    amount = int(input("Enter amount to transfer: "))

    if sender not in accounts or accounts[sender] < amount:
        print("ERROR: Sender does not exist or has insufficient funds.")
        return

    accounts[sender] -= amount
    accounts[receiver] = accounts.get(receiver, 0) + amount
    print(f"{amount} transferred from {sender} to {receiver}.")

def close_account():
    name = input("Enter account name to close: ")
    if name in accounts:
        if accounts[name] == 0:
            del accounts[name]
            print(f"{name}'s account has been closed.")
        else:
            print("ERROR: Account balance must be zero to close.")
    else:
        print("ERROR: Account does not exist.")

def main():
    while True:
        print("\n=== Simple Bank Menu ===")
        print("1. Deposit")
        print("2. Check Balance")
        print("3. Transfer")
        print("4. Close Account")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            deposit()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            transfer()
        elif choice == "4":
            close_account()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
