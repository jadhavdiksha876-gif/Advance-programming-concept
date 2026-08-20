students = {
    "Amit": "CSE",
    "Rahul": "IT",
    "Sneha": "CSE",
    "Priya": "ENTC",
    "Neha": "IT"
}

departments = {}

for name, dept in students.items():
    if dept not in departments:
        departments[dept] = []
    departments[dept].append(name)

print(departments)