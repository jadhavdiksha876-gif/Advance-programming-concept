numbers = [10,20,12,12,50]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("List after removing duplicates:")
print(unique)