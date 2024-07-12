# THE HANGMAN GAME : Step 1

word_list = ["aardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

guess = input("Kindly guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print(letter)
    else:
        print("Wrong")

