str1 = input("Enter a string: ")
rev = ""
for ch in str1:
    rev = ch + rev

if str1 == rev:
    print("Palindrome")
else:
    print("Not Palindrome")