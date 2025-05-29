# Encapsulation: Bank class encapsulates account management logic

class Bank:
    def __init__(self):
        self.accounts = {
        "kay": 1000000,
        "Daniel": 2000000
    }

    def deposit(self, name, amount):
        if name in self.accounts:
            print("Name of account")
        else:
            print("ERROR: Account does not exist.")
            return
        amount = int(input("Enter amount to deposit: "))
        print(f"{amount} deposited into {name}'s account.")

    def balance(self, name):
        if name in self.accounts:
            print(f"Balance for {name}: {self.accounts[name]}")
        else:
            print("ERROR")

    def transfer(self, sender, receiver, amount):
        if sender not in self.accounts or self.accounts[sender] < amount:
            print("ERROR")
            return
        self.accounts[sender] -= amount
        self.accounts[receiver] = self.accounts.get(receiver, 0) + amount
        print(f"Transferred {amount} from {sender} to {receiver}.")

    def close(self, name):
        if name in self.accounts and self.accounts[name] == 0:
            del self.accounts[name]
            print(f"Account {name} closed.")
        else:
            print("ERROR")

# Base class: BankOperation (used for polymorphism)
class BankOperation:
    def run(self, bank):
        raise NotImplementedError("Each operation must implement the run method.")

# Subclass: Deposit (Inheritance + Polymorphism)
class Deposit(BankOperation):
    def run(self, bank):
        name = input("Enter account name: ")
        amount = int(input("Enter amount to deposit: "))
        bank.deposit(name, amount)

# Subclass: Balance
class Balance(BankOperation):
    def run(self, bank):
        name = input("Enter account name to check balance: ")
        bank.balance(name)

# Subclass: Transfer
class Transfer(BankOperation):
    def run(self, bank):
        sender = input("Enter sender's name: ")
        receiver = input("Enter receiver's name: ")
        amount = int(input("Enter amount to transfer: "))
        bank.transfer(sender, receiver, amount)

# Subclass: Close
class Close(BankOperation):
    def run(self, bank):
        name = input("Enter account name to close: ")
        bank.close(name)

# Subclass: Exit
class Exit(BankOperation):
    def run(self, bank):
        print("Exiting banking system.")
        return "EXIT"

# Menu system using polymorphism
def main():
    bank = Bank()
    operations = {
        "1": Deposit(),
        "2": Balance(),
        "3": Transfer(),
        "4": Close(),
        "5": Exit(),
    }

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Check Balance")
        print("3. Transfer")
        print("4. Close Account")
        print("5. Exit")
        choice = input("Select an option: ")

        operation = operations.get(choice)
        if operation:
            result = operation.run(bank)
            if result == "EXIT":
                break
        else:
            print("Invalid choice. Please try again.")

main()
