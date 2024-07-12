# Write a Programm that converts the students scores to Grades

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# Create an empty dictionary called student_grades.

student_grades = {} #this is what we gonna fill up using our programm. should contain student names as key and grades as value

# Write your code below to add the grades to student_grades.👇

for student in student_scores:
  score = student_scores[student]   # in order to access that student score
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectation"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"



# 🚨 Don't change the code below 👇
print(student_grades)