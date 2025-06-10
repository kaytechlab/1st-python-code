class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def choose(self):
        raise NotImplementedError("This method should be overridden.")
import random

class Computer(Player):
    def choose(self):
        return random.choice(["rock", "paper", "scissors"])
class Human(Player):
    def choose(self):
        while True:
            choice = input("Enter rock, paper, or scissors: ").lower()
            if choice in ["rock", "paper", "scissors"]:
                return choice
            else:
                print("Invalid input. Please try again.")

class Game:
    def __init__(self):
        self.human = Human("You")
        self.computer = Computer("Computer")

    def decide_winner(self, human_choice, computer_choice):
        print(f"\nYou chose: {human_choice}")
        print(f"Computer chose: {computer_choice}")

        if human_choice == computer_choice:
            print("It's a tie!")
        elif (human_choice == "rock" and computer_choice == "scissors") or \
             (human_choice == "paper" and computer_choice == "rock") or \
             (human_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            self.human.score += 1
        else:
            print("Computer wins this round!")
            self.computer.score += 1

        print(f"Score => You: {self.human.score} | Computer: {self.computer.score}\n")

    def play(self):
        print("Welcome to Rock-Paper-Scissors!")
        print("First to score 3 points wins the game.\n")

        while self.human.score < 3 and self.computer.score < 3:
            human_choice = self.human.choose()
            computer_choice = self.computer.choose()
            self.decide_winner(human_choice, computer_choice)

        if self.human.score == 3:
            print("Congratulations, you won the game!")
        else:
            print("Computer wins the game. Better luck next time!")
        if __name__ == "__main__":
         game = Game()
         game.play()

