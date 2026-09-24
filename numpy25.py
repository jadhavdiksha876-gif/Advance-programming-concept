import numpy as np
a = np.random.randint(1, 101, size=(3, 4, 5))

print("Original 3D Array:")
print(a)

b = a.flatten()

average = np.mean(b)

print("\nFlattened Array:")
print(b)

print("\nElements greater than 50:")
print(b[b > 50])

print("\nEven numbers:")
print(b[b % 2 == 0])

print("\nAverage:", average)

print("\nElements less than average:")
print(b[b < average])