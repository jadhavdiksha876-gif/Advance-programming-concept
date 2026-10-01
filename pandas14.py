import pandas as pd

df = pd.read_csv("emplyes.csv")

print("CSE Employees:")
print(df[df["Department"] == "CSE"])

print("\nAverage salary:")
print(df["Salary"].mean())

print("\nHighest salary:")
print(df["Salary"].max())

print("\nLowest salary:")
print(df["Salary"].min())

print("\nSalary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise average salary:")
print(df.groupby("Department")["Salary"].mean())