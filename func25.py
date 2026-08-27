books = {
    "Python": True,
    "Java": True,
    "C Programming": False
}

def add_book(name):
    books[name] = True
    print("Book added successfully.")

def issue_book(name):
    if name in books and books[name] == True:
        books[name] = False
        print("Book issued.")
    else:
        print("Book is not available.")

def return_book(name):
    if name in books:
        books[name] = True
        print("Book returned.")
    else:
        print("Book not found.")

def search_book(name):
    if name in books:
        print("Book found.")
    else:
        print("Book not found.")

def display_books():
    print("\nAvailable Books:")
    for name in books:
        if books[name] == True:
            print(name)

add_book("HTML")
issue_book("Python")
return_book("C Programming")
search_book("Java")
display_books()