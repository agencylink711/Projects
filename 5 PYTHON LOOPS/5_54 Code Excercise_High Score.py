
# Print out the highest Number from a List of Numbers using FOR LOOP
# we are replicating the Python .max function with the for loop method
import random

# Generated a bunch of numbers as my student scores with the random module and the range function

# numbers = list(range(34, 47))
# random.shuffle(numbers)
# print(numbers)

student_scores = [34, 41, 46, 36, 35, 40, 44, 45, 37, 43, 42, 39, 38]
for n in range(len(student_scores)):
    student_scores[n] = int(student_scores[n])

# the for loop to track the highest score. First we create a variable and set it to 0
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest Student Score in the list is: {highest_score}")

