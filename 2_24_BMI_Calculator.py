#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# TODO The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)

#I need to store the datatypes into their appropriate Datatypes in Python

height = 1.63
weight = 69

height_as_float = float(height)
weight_as_int = int(weight)

#using the exponent operator (raising the height to a power of 2)
bmi = weight_as_int / height_as_float ** 2
print(bmi)

bmi_as_int = int(bmi)
print(bmi_as_int)