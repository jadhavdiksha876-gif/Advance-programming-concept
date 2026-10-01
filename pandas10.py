import pandas as pd

prices = {
    "Laptop": 50000,
    "Mobile": 25000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Printer": 12000
}

s = pd.Series(prices)

print("Products and prices:")
print(s)

s = s * 1.10

print("\nPrices after 10% increase:")
print(s)

print("\nMost expensive product:")
print(s.idxmax())

print("\nProducts costing more than 1000:")
print(s[s > 1000])