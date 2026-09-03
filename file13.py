file = open("student.txt", "r")
search_word = input("Enter word to search: ")
count = 0
line_numbers = []

line_no = 0

for line in file:
    line_no = line_no + 1
    words = line.split()

    for word in words:
        if word.lower() == search_word.lower():
            count = count + 1
            line_numbers.append(line_no)

file.close()

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)