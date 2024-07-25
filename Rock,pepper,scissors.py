#The following code is a game name rock, pepper, scissors.
import random

user = input("Choose between Rock, Paper, Scissor: ")
print("Your choose",user)

options = ("Rock", "Paper", "Scissor")
computer = random.choice(options)
print("Computer choose", computer)

if user == computer:
    print("You both choose the same! It's a draw!")
elif user == "Rock" and computer == "Paper":
    print("You lose")
elif user == "Rock" and computer == "Scissor":
    print("Your Win")
elif user == "Pepper" and computer == "Rock":
    print("You win!")
elif user == "Pepper" and computer == "Scissor":
    print("You lose")    
elif user == "Scissor" and computer == "Pepper":
    print("Your Win!")
elif user == "Scissor" and computer == "Rock":
    print("Your lose")
