list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
result = list(map(lambda a, b: a + b, list1, list2))
print("Sum:", result)