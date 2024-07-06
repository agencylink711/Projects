'''
LISTS DOCUMENTATION:
https://docs.python.org/3/tutorial/datastructures.html
'''


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana",
                     "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
                     "Arizona", "Alaska", "Hawaii"]


print(states_of_america[0])
print(states_of_america[-1])


# change/alter value in the LIST
states_of_america[1] = "PENCILVANIA"
print(states_of_america)


# add / append to a list
states_of_america.append("Petesylvania")


# extend - add a whole bunch of new list to the existing list
states_of_america.extend(["Petieusa", "PetrousAmericanos", "PeteBamBinoLand", "PetrousLosVegas"])


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
               "Pears", "Tomatoes", "Celery", "Potatoes"]