from string_utils import count_vowels, reverse_string
from string_utils import is_palindrome, count_words, remove_spaces

text = input("Enter a string: ")

print("Vowels:", count_vowels(text))
print("Reverse:", reverse_string(text))
print("Palindrome:", is_palindrome(text))
print("Words:", count_words(text))
print("Without spaces:", remove_spaces(text))