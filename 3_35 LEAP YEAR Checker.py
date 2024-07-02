# LEAP YEAR CALCULATOR
# Our formular checks if the Year inputed is divisible by 4
# Except every year that is evenly divisible by 100 with no remainder
# Unless the year is also divisible by 400 with no remainder

print("Welcome to our LEAP YEAR CALCULATOR")

# We get hold of the year as (a variable) an integer so we can work with it
year = int(input("Kindly enter a year of your choice here: "))

# this checks if year is cleanly divisible by 4 with no remainder, etc.
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 (will also work)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"CONGRATES: your year of Choice: '{year}' is a leap year")
else:
    print(f"SORRY: your year of Choice: '{year}' is NOT a leap year")

