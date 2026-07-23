x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))

if x<y and x<z:
    print("first is smallest value.")
elif y<x and y<z:
    print("second is smallest.")
else:
    print("third is smallest.")