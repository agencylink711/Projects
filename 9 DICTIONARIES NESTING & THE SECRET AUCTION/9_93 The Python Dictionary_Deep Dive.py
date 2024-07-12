programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Retrieving Items from a Dictionary
print(programming_dictionary["Function"])

# Adding new items to the dictionary
programming_dictionary["Loop"] = "The Action of doing something over and over again"
print(programming_dictionary)

# Create an empty dictionary
programming_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A Moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])