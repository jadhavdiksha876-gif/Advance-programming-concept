import re

text = """
# This is a comment
x = 10  # Another comment
print("Hello")
"""

result = re.findall(r'#.*', text)

print("Comments:", result)