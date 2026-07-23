x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))

if x>y and x>z:
    print("first is greater.")
elif y>x and y>z:
    print("second is greater.")
else:
    print("third is greater.")