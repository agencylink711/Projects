# Write your code below this line 👇
# number of cans = (wall height x wall width) ÷ coverage per can.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

import math

test_h = int(input("What is the height of your wall in meters?: ")) # Height of wall (m)
test_w = int(input("What is the width of your wall in meters?: ")) # Width of wall (m)
coverage = 5

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    rounded_up_cans = math.ceil(number_of_cans)
    print(f"You'll need {rounded_up_cans} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage)



