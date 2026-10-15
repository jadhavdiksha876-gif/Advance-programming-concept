import re

email = input("Enter email address: ")

pattern = r'^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$'

if re.fullmatch(pattern, email):
    print("Valid email")
else:
    print("Invalid email")