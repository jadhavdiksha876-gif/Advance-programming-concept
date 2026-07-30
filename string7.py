str1 = input("Enter a string: ")
result = ""
for ch in str1:
    if ch != " ":
        result = result + ch

print("String without spaces:", result)