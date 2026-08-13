numbers=(34,21,56,43,89,76,23,12)
large=numbers[0]
small=numbers[0]
for i in numbers:
    if i>large:
        large=i
    if i<small:
        small=i
print("large:",large)  
print("small:",small)        
