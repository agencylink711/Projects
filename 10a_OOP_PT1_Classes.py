# Create a class called "Person" with the following properties:
# - name (string) # - age (integer) # - occupation (string)
# The class should have a constructor that initializes these properties.
# TODO: Create two methods within the class:
# TODO: introduce(): prints a message introducing the person with their name, age, and occupation.
# TODO: change_occupation(new_occupation): updates the occupation of the person.
# TODO: Create two objects of the Person class and test the methods.


class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation


    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years of age and I am a {self.occupation}")


    def change_occupation(self, new_occupation):
        self.occupation = new_occupation


# creating the Person Object
pete = Person("Peter von Dzerzawa", "42", "Software Engineer")
thomas = Person("Thomas Mueller", "54", "Developer")
daniela = Person("Daniela Mustermann", "63", "Executive Director")
caroline = Person("Caroline Schmidt", "27", "Python Engineer")


caroline.introduce()
pete.introduce()

caroline.change_occupation("Senior Software Engineer")
print(caroline.occupation)

