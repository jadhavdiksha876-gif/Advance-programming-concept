import numpy as np
a = np.arange(1, 25).reshape(2, 3, 4)
print("Original 3D Array:")
print(a)
b = a.flatten()
print("Flattened Array:")
print(b)