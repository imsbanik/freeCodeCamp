import random

def getchoices():
    playerChoice = input("Enter a choice (rock/paper/scissors): ")
    computerOptions = ["rock", "paper", "scissors"]
    computerChoice = random.choice(computerOptions)
    choices = {"player": playerChoice,"computer": computerChoice}
    return choices

def checkWin(player,computer):
    print(f"You chose: {player}, Computer chose: {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "You won"
        else:
            return "You lose"
    elif player == "paper":
        if computer == "rock":
            return "You won"
        else:
            return "You lose"


choices = getchoices()
result = checkWin(choices["player"],choices["computer"])
print(result)