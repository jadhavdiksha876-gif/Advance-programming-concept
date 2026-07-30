n=int(input("Enter the numbers:"))
rev = 0
temp = n
while n>0:
    a=n%10
    rev=(rev*10)+a
    n=n//10
print(rev)