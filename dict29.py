books = {
    101: "Python",
    102: "Java",
    103: "C Programming"
}
books[104] = "Database"

id = int(input("Enter book ID: "))

if id in books:
    print("Book:", books[id])
else:
    print("Book not found")

del books[102]

print("All books:")
for id, name in books.items():
    print(id, ":", name)

print("Total books:", len(books))