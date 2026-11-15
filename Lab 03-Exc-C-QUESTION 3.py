# Excercise C Question 2: PYTHON PROGRAMS
course1 = int(input("Enter Course 1 Marks: "))
course2 = int(input("Enter Course 2 Marks: "))
course3 = int(input("Enter Course 3 Marks: "))
course4 = int(input("Enter Course 4 Marks: "))
course5 = int(input("Enter Course 5 Marks: "))

total = course1 + course2 + course3 + course4 + course5

average = total / 5
percentage = (total / 250) * 100

print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage, "%")