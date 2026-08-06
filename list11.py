n=[10,20,30,40,50,60,70,80,90,100]
print("First 5 elements:")
for i in range(0,5):
    print(n[i])
print("last 5 elements:")
for i in range(-5,0):
    print(n[i])
print("Middle 4 elements:")
for i in range(3,7):
    print(n[i])
print(n[::-1])