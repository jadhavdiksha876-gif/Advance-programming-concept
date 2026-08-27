employees = [
    ("Diksha", "IT", 60000),
    ("Riya", "HR", 45000),
    ("Rahul", "IT", 75000),
    ("Sneha", "Sales", 55000),
    ("Pooja", "HR", 40000)
]

def high_salary(employees):
    return list(filter(lambda emp: emp[2] > 50000, employees))


def increase_salary(employees):
    return list(map(
        lambda emp: (emp[0], emp[1], emp[2] * 1.10),
        employees
    ))

def sort_salary(employees):
    return sorted(employees, key=lambda emp: emp[2])


print("Employees earning more than ₹50,000:")
print(high_salary(employees))

print("\nSalaries after 10% increase:")
print(increase_salary(employees))

print("\nEmployees sorted according to salary:")
print(sort_salary(employees))