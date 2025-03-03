# It's the end of the semester and you got your grades from three classes: Geometry, Algebra, # and Physics.

# Create a program that:

# Reads the grades of these 3 classes (Grades range from 0 - 10)
# Calculate the average of your grades
# Example: Geometry = 6, Algebra = 7, Physics = 8
# Output: average_score = 7
# Warning! Do not use the programming language MAGIC. After you complete the exercise feel
# free to do so.'''

# Read the grades of these 3 classes (Grades range from 0 - 10)

geometry_grade = int(input("Enter your geometry grade (0-10): "))

algebra_grade = int(input("Enter your algebra grade (0-10): "))

physics_grade = int(input("Enter your physics grade (0-10): "))

grades = [geometry_grade, algebra_grade, physics_grade]

number_of_grades = len(grades)

avg_of_grades = int(sum(grades)/number_of_grades)

print(f"Your average grade is: {avg_of_grades}")
