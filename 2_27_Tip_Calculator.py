#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

print("Welcome to the tip Calculator 🧮")
bill = float(input("What was the total Bill? $ "))
tip = int(input("What percentage Tip would you like to give?"
                " Do not add the % sign (10, 12 or 15)?: "))
people = int(input("How many people do you wanna split the bill amongst? "))

total_bill = bill * (tip / 100) + bill
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)
#this formular below turns our rounded float into a string. Having both same value variables is possible in python
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${final_amount}")




