file = open("student.txt", "r")
data = file.read()
words = data.split()
count = {}
for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

print("Word occurrences:")

for word in count:
    print(word, ":", count[word])

file.close()