contacts = {
    "Amit": "9876543210",
    "Rahul": "9876501234",
    "Sneha": "9123456780"
}

contacts["Priya"] = "9988776655"

name = input("Enter name to search: ")

if name in contacts:
    print("Phone number:", contacts[name])
else:
    print("Contact not found")

contacts["Amit"] = "9999999999"

del contacts["Rahul"]

print("All contacts:")
for name, number in contacts.items():
    print(name, ":", number)