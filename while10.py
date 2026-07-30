n=int(input("Enter the number :"))
i = 2
temp = 0
while i<n:
    if n%i==0:
        temp = 1
        break
    i+=1
if temp==0:
    print("Prime")
else:
    print("Not prime")