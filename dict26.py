employees = {
    "Amit": 45000,
    "Rahul": 60000,
    "Sneha": 75000,
    "Priya": 40000,
    "Neha": 55000
}
print("Highest salary:", max(employees.values()))
print("Lowest salary:", min(employees.values()))

average = sum(employees.values()) / len(employees)
print("Average salary:", average)

print("Employees earning more than ₹50,000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)