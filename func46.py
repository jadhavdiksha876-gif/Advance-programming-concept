words = ["apple", "banana", "cat", "elephant", "dog"]
words.sort(key=lambda word: len(word))
print("Sorted words:", words)