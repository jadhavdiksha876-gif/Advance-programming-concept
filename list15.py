list = [10,20,30,40,50]
large=list[0]
second = list[1]
for i in list:
    if large < i:
        second = large
        large = i
    elif second<i and second != large:
        second =i
print(second)