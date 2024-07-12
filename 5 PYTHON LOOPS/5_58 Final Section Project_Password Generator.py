import random

# 1. Initialize Lists: Ensure the lists letters, numbers, and symbols are ready for use.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# 2. Gather User Input: Use input() to ask the user how many letters, symbols, and numbers they want in the password.

print("Welcome to the PyPassWord Generator\n")
password_letters = int(input("How many letters would you like in your Password:?\n"))
password_numbers = int(input("How many numbers would you like:? Choose only from 1 to 9 Symbols\n"))
password_symbols = int(input("How many Symbols would you like:? Choose only from 1 to 9 Symbols\n"))


# 3. Generate Random Characters
# Use a loop to randomly select the specified number of letters-symbols-&-numbers from their lists and add them to final_password.

# for n in range(1, password_letters + 1):
    #password += random.choice(letters)

final_password = []

for n in range(1, password_letters + 1):
    final_password.append(random.choice(letters))

for n in range(password_numbers):
    final_password.append(random.choice(numbers))

for n in range(password_symbols):
    final_password.append(random.choice(symbols))

# 4. Shuffle Password:
# Use random.shuffle() function to shuffle the final_password list to ensure the characters are in a random order.

random.shuffle(final_password)

# 5. Convert List to String:
# Convert the final_password list to a string using ''.join(final_password).

password = ""
for n in final_password:
    password += n

# 6. Print the Final Password:

print(f"Here is your final set of Password: {password}")
