#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_lenght = len(chosen_word)
for n in range(word_lenght):
    display += "_"
print(display)


guess = input("Guess a letter: ").lower()


for position in range(word_lenght):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter


print(display)