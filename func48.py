employees = [
    ("Diksha", 30000),
    ("Shreya", 50000),
    ("Seeta", 25000),
    ("Sneha", 45000)
]
employees.sort(key=lambda employee: employee[1])
print("Employees according to salary:")
for employee in employees:
    print(employee)