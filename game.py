import random

print("Welcome to Rock-Paper-Scissors!")

choice = random.choice(["rock", "paper", "scissors"])
p_input = input("Choose rock, paper, or scissors: ")

print("Computer chose: " + choice)
print("You chose: " + p_input)
