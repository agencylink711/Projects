#CODING EXERCISE AND PRACTICE SESSION


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoaster")

    age = int(input("What is your age?"))

    if age < 12:
        print("Please pay $")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("please pay $12")
else:
    print("you are a bit too young")





