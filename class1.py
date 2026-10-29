class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage)
        print()

s1 = Student(1, "Rahul", [80, 75, 90, 85, 70])
s2 = Student(2, "Priya", [85, 90, 88, 80, 92])

s1.display()
s2.display()