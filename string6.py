str1 = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")
result = ""
for ch in str1:
    if ch == old:
        result = result + new
    else:
        result = result + ch

print("New string:", result)