import numpy as np
a = np.array([10, 25, 60, 45, 80, 30, 90, 50, 70, 20])
a[a > 50] = 0
print("Array:", a)