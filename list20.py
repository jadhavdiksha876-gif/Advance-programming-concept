books = []
while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display Books")
    print("5. Count Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)
        print("Book Added.")

    elif choice == 2:
        book = input("Enter book name to search: ")
        if book in books:
            print("Book Found.")
        else:
            print("Book Not Found.")

    elif choice == 3:
        book = input("Enter book name to remove: ")
        if book in books:
            books.remove(book)
            print("Book Removed.")
        else:
            print("Book Not Found.")

    elif choice == 4:
        print("Books:")
        for b in books:
            print(b)

    elif choice == 5:
        print("Total Books:", len(books))

    elif choice == 6:
        break

    else:
        print("Invalid Choice")