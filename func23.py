def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / 5

def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "F"

def class_average(students):
    total = 0

    for student in students:
        total = total + percentage(student["marks"])

    return total / len(students)

def highest_scorer(students):
    highest = students[0]

    for student in students:
        if total_marks(student["marks"]) > total_marks(highest["marks"]):
            highest = student

    return highest

def lowest_scorer(students):
    lowest = students[0]

    for student in students:
        if total_marks(student["marks"]) < total_marks(lowest["marks"]):
            lowest = student

    return lowest

students = [
    {"name": "Amit", "roll": 1, "marks": [80, 75, 90, 85, 70]},
    {"name": "Riya", "roll": 2, "marks": [90, 85, 95, 80, 90]},
    {"name": "Rahul", "roll": 3, "marks": [60, 70, 65, 75, 80]}
]
for student in students:
    total = total_marks(student["marks"])
    percent = percentage(student["marks"])
    g = grade(percent)

    print("\nName:", student["name"])
    print("Roll No:", student["roll"])
    print("Total:", total)
    print("Percentage:", percent)
    print("Grade:", g)

print("\nClass Average:", class_average(students))

high = highest_scorer(students)
low = lowest_scorer(students)

print("Highest Scorer:", high["name"])
print("Lowest Scorer:", low["name"])