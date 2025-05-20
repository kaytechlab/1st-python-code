# Question Title: Simple Bank Account Manager using Dictionary
#
# Description:
#
# You are to build a simple banking system that uses a dictionary to manage user accounts.
# Each account is identified by a name (string), and its value is the account balance (an integer).
#
# You are to implement a function called bank_channel(command: str) that takes a string
# command and performs one of the following actions:
# 	1.	DEPOSIT name amount – Adds amount to name’s account. If the account doesn’t exist, create it with the amount.
# 	2.	BALANCE name – Prints the balance of name’s account. If the account does not exist, print "ERROR".
# 	3.	TRANSFER sender receiver amount – Transfers amount from sender to receiver. If
# 	the sender’s account doesn’t exist or has insufficient funds, print "ERROR". If the receiver doesn’t exist, create it.
# 	4.	CLOSE name – Closes the account and removes it from the system. If the account
# 	doesn’t exist or has a non-zero balance, print "ERROR".
# 	5.	EXIT – Terminates the input.
accounts = {
    "Kay": 1000,
    "Daniel": 500
}
accounts = {}

def bank_channel(command: str):
    parts = command.strip().split()
    if not parts:
        return

    action = parts[0].upper()

    if action == "DEPOSIT":
        if len(parts) != 3:
            print("ERROR")
            return
        name = parts[1]
        amount = int(parts[2])
        if name in accounts:
            accounts[name] += amount
        else:
            accounts[name] = amount

    elif action == "BALANCE":
        if len(parts) != 2:
            print("ERROR")
            return
        name = parts[1]
        if name in accounts:
            print(accounts[name])
        else:
            print("ERROR")

    elif action == "TRANSFER":
        if len(parts) != 4:
            print("ERROR")
            return
        sender = parts[1]
        receiver = parts[2]
        amount = int(parts[3])

        if sender not in accounts or accounts[sender] < amount:
            print("ERROR")
            return

        accounts[sender] -= amount
        if receiver in accounts:
            accounts[receiver] += amount
        else:
            accounts[receiver] = amount

    elif action == "CLOSE":
        if len(parts) != 2:
            print("ERROR")
            return
        name = parts[1]
        if name in accounts and accounts[name] == 0:
            del accounts[name]
        else:
            print("ERROR")

    elif action == "EXIT":
        return "EXIT"

    else:
        print("ERROR")
while True:
    cmd = input(">> ")
    if bank_channel(cmd) == "EXIT":
        break
