products = {
    "Pen": 20,
    "Book": 8,
    "Pencil": 15,
    "Bag": 5
}
products["Bottle"] = 12

products["Pen"] = 25

del products["Pencil"]

name = input("Enter product name to search: ")

if name in products:
    print("Product found. Quantity:", products[name])
else:
    print("Product not found")

print("Products with quantity below 10:")

for name, quantity in products.items():
    if quantity < 10:
        print(name, ":", quantity)