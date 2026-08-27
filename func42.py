numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime = list(filter(
    lambda n: n > 1 and all(n % i != 0 for i in range(2, n)),
    numbers
))
print("Prime numbers:", prime)