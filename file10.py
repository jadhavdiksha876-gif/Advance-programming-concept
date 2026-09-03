file = open("student.txt", "r")
data = file.read()
alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in data:
    if ch.isalpha():
        alphabets = alphabets + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    elif ch != "\n":
        special = special + 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

file.close()