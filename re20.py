import re

text = "Files: report.pdf, photo.jpg, program.py"
result = re.findall(r'\.([A-Za-z0-9]+)\b', text)

print("Extensions:", result)