import random


player1 = input("Enter a hand gesture (rock, paper, scissors, lizard, spock): ")
player2 = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
print(f"Player 2 chose {player2}")

if player1 == player2:
    print("It's a tie!")
elif (player1, player2) in [("rock", "paper"), ("paper", "scissors"), ("scissors", "rock"), ("spock", "rock"), ("lizard", "paper"), ("spock", "scissors"), ("lizard", "spock"), ("paper", "spock"), ("rock", "lizard"), ("scissors", "lizard")]:
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")