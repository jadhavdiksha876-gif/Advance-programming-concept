def calculate(numbers):
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]
    for n in numbers:
        total = total + n
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
    average = total / len(numbers)
    return minimum, maximum, total, average
numbers = [10, 20, 30, 40, 50]
minimum, maximum, total, average = calculate(numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)
print("Average:", average)