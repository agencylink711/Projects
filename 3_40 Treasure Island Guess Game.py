print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


left_right = input("You are at a cross road, where will you want to go? Type left or right: ")
left_right = left_right.lower()


if left_right == "left":
    wait_swim = input("You come to a lake, there is an island in the middle. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    wait_swim = wait_swim.lower()

    if left_right == "swim":
        print("Attacked by trout. GAME OVER 🔥🔥🔥")

    elif wait_swim == "wait":
        door = input("you arrived at the Island unharmed. There is a house with 3 Doors. 'Red', 'Yellow' and 'Blue'. Which door color do you want?:\n")
        door = door.lower()

        if door == "red":
            print("Burned by fire. GAME OVER 🔥🔥🔥")
        elif door == "blue":
            print("eaten by beast. GAME OVER 🔥🔥🔥")
        elif door == "yellow":
            print("YOU 🏆🏆🏆🏆 WINNNNNNN 🏆🏆🏆🏆")
        else:
            print("Wrong choice... GAME OVER 🔥🔥🔥")

else:
    print("You fall into a whole. GAME OVER 🔥🔥🔥")






