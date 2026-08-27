words = ["apple", "banana", "cat", "elephant", "computer", "dog"]

def word_lengths(words):
    return list(map(lambda word: len(word), words))

def long_words(words):
    return list(filter(lambda word: len(word) > 5, words))

def sort_words(words):
    return sorted(words, key=lambda word: len(word))


print("Length of every word:")
print(word_lengths(words))

print("\nWords having more than 5 characters:")
print(long_words(words))

print("\nWords sorted according to length:")
print(sort_words(words))