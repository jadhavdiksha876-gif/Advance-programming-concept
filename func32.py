def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(operation, a, b):
    return operation(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", calculate(add, a, b))
print("Subtraction:", calculate(subtract, a, b))
print("Multiplication:", calculate(multiply, a, b))

if b != 0:
    print("Division:", calculate(divide, a, b))
else:
    print("Cannot divide by zero.")