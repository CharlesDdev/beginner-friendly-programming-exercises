# The exercise is almost identical to a previous exercise with a minor change.
# It's #the end of the semester and you got your marks from, Geometry, Algebra, Physics  # classes.
# If the average score is 7 and above print "Good job!",
# if the average score is between 6 and 4 print "You need to work harder!",
# if the average score is below 4 print "Failed, you really need to work harder!".

# Create a program that:

# Reads the values of these 3 lessons
# Calculate the average of your grades
# Example: Geometry = 6, Algebra = 7, Physics = 8
# Output: Your average score is 7, Good job!"
# Warning! Do not use the programming language magic. After you complete the exercise feel free to do so.

geometry_grade = int(input("Enter your geometry grade (0-10): "))

algebra_grade = int(input("Enter your algebra grade (0-10): "))

physics_grade = int(input("Enter your physics grade (0-10): "))

grades = [geometry_grade, algebra_grade, physics_grade]

number_of_grades = len(grades)

avg_of_grades = int(sum(grades)/number_of_grades)

print(f"Your average grade is: {avg_of_grades}")

if avg_of_grades >= 7:
    print("Good job!")
if avg_of_grades >= 4 and avg_of_grades <= 6:
    print("You need to work harder!")
if avg_of_grades < 4:
    print("Failed, you really need to work harder!")
