numbers = (11, 24, 14, 33, 42, 51, 58, 77, 80, 90, 12, 21, 36, 45, 50)
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even numbers =", even)
print("Odd numbers =", odd)