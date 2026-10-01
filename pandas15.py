import pandas as pd

df = pd.read_csv("patients.csv")

print("Patients above 60:")
print(df[df["Age"] > 60])

print("\nAverage medical expense:")
print(df["Medical_Expense"].mean())

print("\nPatient with highest medical expense:")
print(df.loc[df["Medical_Expense"].idxmax()])

print("\nNumber of patients for each disease:")
print(df["Disease"].value_counts())

print("\nMedical expense greater than 50000:")
print(df[df["Medical_Expense"] > 50000])