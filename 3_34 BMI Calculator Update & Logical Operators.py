
print("Please enter the following information in digits only: ")

height = float(input("What is your current height? "))  # in meters e.g., 1.55
weight = int(input("What is your current weight"))  # in kilograms e.g., 72

# this is the BMI calculator 👇
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, You may be underweight")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, You have a normal weight")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, You are slightly overweight")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, I am sorry to say, but you may be obese")
elif bmi >= 35:
    print((f"your BMI is {bmi}, You may be clinically obese"))