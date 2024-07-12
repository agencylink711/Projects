# CALCULATE THE SUM OF ALL THE EVEN NUMBERS FROM 1 TO 177
# Another way of achieving this is: for number in range(2, target + 1, 2)


range_number = int(input(f"To calculate your dream Event Numbers, \n"
                         f"Enter your dream Number in here: between 10 & 1000: "))


final_sum = 0

for number in range(1, range_number + 1):
    if number % 2 == 0:
        final_sum += number

print(f"the final sum of all even numbers in range of 1 to 177 is: {final_sum}")


