import numpy as np

marks = np.array([
    45, 67, 78, 89, 56,
    92, 73, 65, 88, 49,
    95, 70, 81, 60, 55,
    77, 84, 68, 90, 72
])

average = np.mean(marks)

print("Class Average:", average)

above_average = marks[marks > average]

print("Students scoring above average:")
print(above_average)