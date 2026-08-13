t = (10, 20, 30, 40)
print("Original tuple:", t)
l = list(t)
l[2] = 50
t = tuple(l)
print("Modified tuple:", t)