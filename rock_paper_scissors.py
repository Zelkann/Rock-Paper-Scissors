import random


player1 = input("Enter a hand gesture (rock, paper, scissors): ")
player2 = random.choice(["rock", "paper", "scissors"])
print(f"Player 2 chose {player2}")

if player1 == player2:
    print("It's a tie!")
elif (player1, player2) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")