file = open("student.txt", "r")
data = file.read()
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

data = data.replace(old_word, new_word)

file.close()

new_file = open("new_student.txt", "w")
new_file.write(data)
new_file.close()

print("Word replaced successfully.")
print("Modified file saved as new_student.txt")