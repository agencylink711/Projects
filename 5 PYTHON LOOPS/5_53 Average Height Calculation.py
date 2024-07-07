

# The next 3 lines of code will turn student_heights into a list

student_heights = ["151", "145", "179"]
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

total_height = 0
for height in student_heights:
    total_height += height
print(f"total Height = {total_height}")


number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"Number of Students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"Average height = {average_height}")