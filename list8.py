n=[12,34,2,4,6,5,89,67,0,1,23,45,76,98,13]
even = 0
odd = 0
for i in n:
    if i%2==0:
        even += 1
    else:
        odd += 1
print("even : ",even)
print("odd : ",odd)
