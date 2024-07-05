# PIZZA ORDER PROGRAMM

print("Thank you for choosing Python Pizza Deliveries!\n")

size = input("What 'PIZZA SIZE' do You wanna have? S, M or L?: ")

bill = 0

if size == "S":
    bill = 15
    print(f"Your Bill status is now: ${bill}")

    pepperoni_s = input("$2 Extra for Pepperoni to your 'PIZZA'? Y or N?: ")
    bill += 2
    print(f"Your Bill status is now: ${bill}.")

elif size == "M":
    bill = 20
    print(f"Your Bill status is now: ${bill}")

    pepperoni_m = input("$3 Extra for Pepperoni to your 'PIZZA'? Y or N?: ")
    bill += 3
    print(f"Your Bill status is now: ${bill}.")

elif size == "L":
    bill = 25
    print(f"Your Bill status is now: ${bill}")

    pepperoni_l = input("$3 Extra for Pepperoni to your 'PIZZA'? Y or N?: ")
    bill += 3
    print(f"Your Bill status is now: ${bill}.")

    cheese = input("$1 only for Extra Cheese. Y or N?: ")
    if cheese == "Y":
        bill += 1
    else:
        bill == bill


print(f"Thank You for choosing 'Python Pizza', your Final Bill is : ${bill}.")