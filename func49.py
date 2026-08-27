students = [
    ("Dikshan", 80),
    ("Riya", 90),
    ("Rahul", 65),
    ("Sneha", 75),
    ("Pooja", 85)
]

def average_marks(students):
    marks = list(map(lambda student: student[1], students))
    return sum(marks) / len(marks)

def above_75(students):
    return list(filter(lambda student: student[1] > 75, students))

def sort_students(students):
    return sorted(students, key=lambda student: student[1])

print("Average Marks:", average_marks(students))

print("\nStudents scoring above 75:")
print(above_75(students))

print("\nStudents sorted according to marks:")
print(sort_students(students))