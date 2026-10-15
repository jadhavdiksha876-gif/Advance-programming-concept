import re

text = "My PIN is 416001 and another PIN is 411001"
result = re.findall(r'\b[1-9]\d{5}\b', text)

print("PIN codes:", result)