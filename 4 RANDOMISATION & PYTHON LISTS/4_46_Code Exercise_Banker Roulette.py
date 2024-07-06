'''
PICK A RANDOM NAME FROM A LIST of names to pay a Bill
Important: You are not allowed to use the choice() function.

NOTE: In this exercise, you are working collaboratively with another programmer.
They already dealt with input() and writing the code needed to get hold of the names in the input area,
so you don't need to worry about that.

The other programmer has written the code to separate the names in the input area into individual names
and puts them inside a List called names.
For their code to work correctly, you must enter all the names in the input area followed by comma then space.
e.g. name, name, name

You can try printing names to see what it looks like (but remember to remove that code when you submit the assignment).
Assume that names works like this:

input area: x, y, z,
names = ["x", "y", "z"]
Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!
Hints
You might need the help of the len() function. https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list

Remember that Lists start at index 0!
'''

import random


names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

print("Hello Everyone: We are always glad to have you eat for free\n")
print("However: Today 1 of you have been randomly picked to pay the bill\n")


# 1. getting hold of the total number of items in the list [positional arguements]
number_of_items = len(names)

# 2. Generate random number between 0 and the last index. taking the number of items, subtracting it by 1 (because lists starts from 0 then to the last index in the list)
random_choice = random.randint(0, number_of_items - 1)

# 3. choose and print a random name.
final_random_choice = (names[random_choice])



print(f"yaaaaa, -> {final_random_choice}. <- is going to buy the meal today. Hurraaayyy 🎉")




