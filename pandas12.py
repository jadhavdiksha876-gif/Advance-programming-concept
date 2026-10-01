import pandas as pd

attendance = {
    "Amit": 80,
    "Priya": 92,
    "Rahul": 70,
    "Sneha": 95,
    "Neha": 65
}

s = pd.Series(attendance)

print("Average attendance:")
print(s.mean())

print("\nAttendance below 75:")
print(s[s < 75])

print("\nAttendance above 90:")
print(s[s > 90])

print("\nHighest attendance:")
print(s.max())