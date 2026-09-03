file = open("student.txt", "r")
new_file = open("uppercase.txt", "w")
data = file.read()
new_file.write(data.upper())

file.close()
new_file.close()

print("Text copied in uppercase successfully.")