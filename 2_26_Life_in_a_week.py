# Create a program using maths and f-Strings that tells us how many weeks we have left,
# if we live until 90 years old.
# Practicing using F-Strings for our Printed Outputs



current_age = 41
expected_age = 90
weeks_in_year = 52

age_left = expected_age - current_age

weeks_left = age_left * weeks_in_year

print(weeks_left)

print(f"hello, you have approximately {weeks_left} weeks left to live if you are gonna be {expected_age} years old")

