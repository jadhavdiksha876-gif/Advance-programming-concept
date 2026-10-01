import pandas as pd

salary = {
    "Amit": 45000,
    "Priya": 60000,
    "Rahul": 55000,
    "Sneha": 70000,
    "Neha": 48000
}

s = pd.Series(salary)

print("Series:")
print(s)

print("\nHighest salary:")
print(s.max())

print("\nLowest salary:")
print(s.min())

print("\nAverage salary:")
print(s.mean())

print("\nEmployees earning more than 50000:")
print(s[s > 50000])