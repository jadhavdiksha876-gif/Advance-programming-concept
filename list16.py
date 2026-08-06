students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print("\nEnter details of Student", i + 1)
    
    name = input("Enter Name: ")
    roll = int(input("Enter Roll Number: "))
    marks = float(input("Enter Marks: "))
    
    students.append([name, roll, marks])

print("\nStudent Details:")
for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()