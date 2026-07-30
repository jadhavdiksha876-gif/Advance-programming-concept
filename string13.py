s = input("Enter a sentence:")
word = s.split()
shortest = word[0]
for word in word:
    if len(word) < len(shortest):
        shortest = word
print("Shortest word:",shortest)
