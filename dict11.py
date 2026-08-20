students = {"Amit": 75,"Rahul": 88,"Sneha": 92,"Priya": 81}
highest = max(students, key=students.get)
print("Student with highest marks:", highest)
print("Marks:", students[highest])