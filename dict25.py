students = {"Amit": 75,"Rahul": 85,"Sneha": 92}
students["Priya"] = 88
students["Amit"] = 80

del students["Rahul"]
name = input("Enter student name to search: ")

if name in students:
    print("Student found. Marks:", students[name])
else:
    print("Student not found")

print("All students:")
for name, marks in students.items():
    print(name, ":", marks)

highest = max(students.values())
print("Highest marks:", highest)

average = sum(students.values()) / len(students)
print("Average marks:", average)