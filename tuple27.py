tuple1 = (10,20,30,40)
tuple2 = (40,50,60,70)
merged = tuple1 + tuple2
result = ()
for i in merged:
    if i not in result:
        result = result + (i,)
print("Merged tuple =", result)