tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)
common = ()
for i in tuple1:
    if i in tuple2:
        common = common + (i,)
print("Common elements =", common)