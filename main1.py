from number_utils import is_prime, is_palindrome, is_armstrong, is_perfect

n = int(input("Enter a number: "))

if is_prime(n):
    print("Prime number")
else:
    print("Not a prime number")

if is_palindrome(n):
    print("Palindrome number")
else:
    print("Not a palindrome number")

if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")

if is_perfect(n):
    print("Perfect number")
else:
    print("Not a perfect number")