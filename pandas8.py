import pandas as pd

marks = {
    "Amit": 80,
    "Priya": 90,
    "Rahul": 70,
    "Sneha": 85,
    "Neha": 95
}

s = pd.Series(marks)

print("Series:")
print(s)

print("\nMarks of Priya:")
print(s["Priya"])

print("\nMaximum marks:")
print(s.max())

print("\nMinimum marks:")
print(s.min())

print("\nAverage marks:")
print(s.mean())

print("\nStudents scoring more than 75:")
print(s[s > 75])