import pandas as pd

ages = {
    "P001": 65,
    "P002": 45,
    "P003": 70,
    "P004": 30,
    "P005": 62
}

s = pd.Series(ages)

print("Average age:")
print(s.mean())

print("\nOldest patient:")
print(s.idxmax(), s.max())

print("\nYoungest patient:")
print(s.idxmin(), s.min())

print("\nPatients above 60:")
print(s[s > 60])