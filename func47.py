students = [
    ("Diksha", 95),
    ("Minal", 90),
    ("Seeta", 65),
    ("Sneha", 85)
]
students.sort(key=lambda student: student[1])
print("Students according to marks:")
for student in students:
    print(student)