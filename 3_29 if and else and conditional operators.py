#CODING EXERCISE AND PRACTICE SESSION


print("Welcome to the Rollercoaster 🎢 of the FUTURE!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("you can ride the rollercoaster")

    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay: Child Tickets are -> $5")
    elif age <= 18:
        bill = 7
        print("Please pay: Youth tickets are -> $7.")
    elif age >= 45 and age <= 55:
        print("You can ride for free")
    else:
        bill = 12
        print("Please pay: Adult tickets are -> $12")

    wants_photo = input(f"Do you want a Photo taken as an additional service? Kindly type y or n ")
    if wants_photo == "Y":
        #Add $3 to their bill
        bill += 3
    print(f"Your final bill is '${bill}'")

else:
    print("you are a bit too young")





