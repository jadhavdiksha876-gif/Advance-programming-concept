s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
if len(items) >= 2:
    print("Second most frequent character:", items[1][0])
else:
    print("No second most frequent character")