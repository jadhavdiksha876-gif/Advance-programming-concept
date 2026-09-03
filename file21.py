file = open("books.txt", "w")

file.write("101,Python Programming,John,Available\n")
file.write("102,Java Programming,James,Available\n")
file.write("103,Data Structures,Robert,Available\n")

file.close()


def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    file = open("books.txt", "a")
    file.write(book_id + "," + title + "," + author + ",Available\n")
    file.close()

    print("Book added successfully.")


def search_book():
    search_id = input("Enter book ID: ")

    file = open("books.txt", "r")

    found = False

    for line in file:
        data = line.strip().split(",")

        if data[0] == search_id:
            print("Book ID:", data[0])
            print("Title:", data[1])
            print("Author:", data[2])
            print("Status:", data[3])
            found = True

    file.close()

    if not found:
        print("Book not found.")


def issue_book():
    book_id = input("Enter book ID to issue: ")

    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("books.txt", "w")

    found = False

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            if data[3] == "Available":
                data[3] = "Issued"
                found = True
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
                found = True

            line = ",".join(data) + "\n"

        file.write(line)

    file.close()

    if not found:
        print("Book not found.")


def return_book():
    book_id = input("Enter book ID to return: ")

    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("books.txt", "w")

    found = False

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Available"
            line = ",".join(data) + "\n"
            found = True
            print("Book returned successfully.")

        file.write(line)

    file.close()

    if not found:
        print("Book not found.")


def display_available():
    file = open("books.txt", "r")

    print("\nAvailable Books:")

    for line in file:
        data = line.strip().split(",")

        if data[3] == "Available":
            print(data[0], data[1], data[2])

    file.close()


while True:
    print("\n--- Book Management System ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        display_available()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")