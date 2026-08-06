city= ["Kolhapur","satara","Sanngali","Nashik"]
l=input("Enter a string: ")
found = False
for i in city:
    if l == i:
        print("YES")
        found = True
if found == False:
    print("NO")