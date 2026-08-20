students = {"Amit": 75,"Rahul": 88,"Sneha": 92,"Priya": 81}
lowest = min(students, key=students.get)
print("Student with lowest marks:", lowest)
print("Marks:", students[lowest])