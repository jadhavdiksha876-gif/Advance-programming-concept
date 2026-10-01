import pandas as pd
data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Student_Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Python": [80, 70, 90, 85, 75],
    "DBMS": [75, 80, 85, 90, 70],
    "Mathematics": [85, 75, 80, 95, 78]
}

df = pd.DataFrame(data)

print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average:")
print(df)

print("\nStudents with average greater than 75:")
print(df[df["Average"] > 75])