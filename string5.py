str1 = input("Enter a string: ")

upper = 0
lower = 0

for ch in str1:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1

print("Uppercase letters =", upper)
print("Lowercase letters =", lower)