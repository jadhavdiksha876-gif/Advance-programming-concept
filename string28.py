s = input("Enter paragraph: ")
words = s.split()
for word in set(words):
    print(word,"=",word.count(word))