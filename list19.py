students = []
n = int(input("Enter number of students present: "))
for i in range(n):
    name = input("Enter student name: ")
    students.append(name)

while True:
    print("\n1. Total Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Remove Student")
    print("5. Display Students")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Total Students:", len(students))

    elif choice == 2:
        name = input("Enter student name to search: ")
        if name in students:
            print(name, "is Present")
        else:
            print(name, "is Absent")

    elif choice == 3:
        name = input("Enter new student name: ")
        students.append(name)
        print("Student Added.")

    elif choice == 4:
        name = input("Enter absent student name: ")
        if name in students:
            students.remove(name)
            print("Student Removed.")
        else:
            print("Student Not Found.")

    elif choice == 5:
        print("Students Present:")
        for s in students:
            print(s)

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")