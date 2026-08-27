products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 3),
    ("Keyboard", 1200, 2),
    ("Monitor", 15000, 1),
    ("Pen", 20, 10)
]
def total_value(products):
    return list(map(
        lambda product: (
            product[0],
            product[1],
            product[2],
            product[1] * product[2]
        ),
        products
    ))

def costly_products(products):
    return list(filter(
        lambda product: product[1] > 1000,
        products
    ))

def sort_by_value(products):
    return sorted(
        products,
        key=lambda product: product[1] * product[2]
    )


print("Total value of each product:")
print(total_value(products))

print("\nProducts costing more than ₹1,000:")
print(costly_products(products))

print("\nProducts sorted according to total value:")
print(sort_by_value(products))