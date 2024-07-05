# Using only [if, elif or else] Writing a program that tests the compatibility between two people
# TODO: Take both people's names and check for the number of times the letters in the word TRUE occurs
# TODO: Then check for the number of times the letters in the word LOVE occurs

# 1. Grabbing the names as inputs to work with and converting them into strings
name1 = str(input(f"Kindly type in the full 'Female' name in this field: "))
name2 = str(input(f"Kindly type in the full 'Male' name in this field: "))

# 2. Converting all inputs into lower case with .(lower)
name1 = name1.lower()
name2 = name2.lower()
combined_names = name1 + name2

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
first_digit = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your 'Love Score' is: {score}, you match pretty well.")

elif (score >= 40) and (score <= 50):
    print(f"Your 'Love Score' is: {score}, you are okay together")

else:
    print(f"Your 'Love Score' is: {score}")









