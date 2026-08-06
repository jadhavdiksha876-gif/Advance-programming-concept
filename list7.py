print("Enter 10 elements:")
a=[]
sum=0
for i in range(10):
    a.append(int(input()))
    sum=sum+a[i]
print(a)
print(sum)
avg=sum/10
print(avg)