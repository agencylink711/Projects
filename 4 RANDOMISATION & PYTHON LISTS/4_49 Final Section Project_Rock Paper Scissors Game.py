# THE GAME RULES ARE
# * Rock wins against scissors. * Scissors win against Paper. * Paper wins against Rock.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# positional arguements for images
game_images = [rock, paper, scissors]

# Generating a number between 0 & 2, so we have our proxy for our choices
# choice = ["rock", "paper", "scissors"]
# random_choice = random.randint(0, choice - 1)

print("--> You are now playing ROCK PAPER SCISSORS against a --> COMPUTER <-- \n")

# Generating the Choices  to be made
user_choice = int(input("--> Time to make your choice: Kindly type in 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid Number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("computer chose:")
    print(game_images[computer_choice])


    # Generating the GAME logic
    if user_choice == 0 and computer_choice == 2:
        print("YOU WIN!")
    elif user_choice == 1 and computer_choice == 0:
        print("YOU WIN")
    elif computer_choice == 0 and user_choice == 2:
        print("You LOSE")
    elif computer_choice > user_choice:
        print("You LOSE")
    elif user_choice == computer_choice:
        print("We have a DRAW")


