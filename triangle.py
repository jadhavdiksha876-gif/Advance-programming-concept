n = int(input("Enter the value of n: "))
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    for j in range(i + 1):
        print(letters[j],end=" ")
    print()