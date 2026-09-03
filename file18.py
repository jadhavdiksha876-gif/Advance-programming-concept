file = open("employees.txt", "w")

file.write("101,Amit,IT,50000\n")
file.write("102,Priya,HR,60000\n")
file.write("103,Rahul,Sales,45000\n")
file.write("104,Neha,IT,75000\n")

file.close()


def read_employees():
    file = open("employees.txt", "r")

    employees = []

    for line in file:
        data = line.strip().split(",")

        employee = {
            "id": data[0],
            "name": data[1],
            "department": data[2],
            "salary": float(data[3])
        }

        employees.append(employee)

    file.close()

    return employees


def display_all(employees):
    print("All Employees:")

    for e in employees:
        print(e["id"], e["name"], e["department"], e["salary"])



def highest_paid(employees):
    employee = max(employees, key=lambda x: x["salary"])

    print("\nHighest Paid Employee:")
    print(employee["name"], employee["salary"])



def average_salary(employees):
    total = 0

    for e in employees:
        total = total + e["salary"]

    average = total / len(employees)

    print("\nAverage Salary:", average)


def above_salary(employees, salary):
    print("\nEmployees earning above", salary)

    for e in employees:
        if e["salary"] > salary:
            print(e["name"], e["salary"])



employees = read_employees()

display_all(employees)

highest_paid(employees)

average_salary(employees)

salary = float(input("\nEnter salary: "))

above_salary(employees, salary)