dictionary={
    "human": 0,
    "computer": 0
}
games = ['rock', 'paper', 'scissors']

print(" Welcome to Rock-Paper-Scissors!")
print("First to 3 points wins the game.\n")
while human_score < 3 and computer_score < 3:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in options:
        print("Invalid choice. Please try again.\n")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("You win this round!")
        human_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score => You: {human_score} | Computer: {computer_score}\n")

if human_score == 3:
    print("You won the game!")
else:
    print("Computer won the game!")
