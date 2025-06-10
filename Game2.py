# class player:
#     def __init__(self, name):
#         self.name = name
#         self.score = 0
# import random
# class computer(player):
#     def choose(self):
#         return random.choice(["rock","Paper","scissors"])
# class Human(player):
#     def choose(self):
#         while True:
#             choice = input("Enter rock, paper, scissors: ")
#             if choice in ["rock, paper", "scissors"]:
#                 return choice
#             else:
#                 print("Invalid input")
#
# class game:
#     def __init__(self):
#         self.Human= Human("you")
#         self.computer = computer("computer")
import random
score={
    "player": 0,
    "computer": 0
}
game =["rock","paper","scissors"]

while score["player"] < 3 and score["computer"] < 3:
    user_choice = input("Choose rock, paper, or scissors: ")
    if user_choice not in game:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(game)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("You win this round!")
        score["player"] += 1
    else:
        print("Computer wins this round!")
        score["computer"] += 1

    print(f"Score => You: {"player"} | Computer: {"computer"}")

if score ["player"] == 3:
    print("You won the game!")
else:
    print("Computer won the game!")