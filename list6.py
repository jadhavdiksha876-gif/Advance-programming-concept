l=[10,20,30,40,50]
large=l[0]
small=l[0]
for i in l:
    if large<i:
        large = i
    if small>i:
        small =i
print(large)
print(small)