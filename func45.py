words = ["apple", "banana", "cat", "elephant", "computer", "dog"]
result = list(filter(lambda word: len(word) > 5, words))
print("Words:", result)