line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

# 1. your program must take the user input and convert it to a usable format

position = input("b3") # Where do you want to put the treasure?


letter = position[0].lower()
abc = ["a", "b", "c"]
# in order to do the comparison, we use a method that comes from the python list called (.index)
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")