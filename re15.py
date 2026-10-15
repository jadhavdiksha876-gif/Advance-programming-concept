import re

text = "Learning #Python and #Programming is fun"
result = re.findall(r'(?<!\w)#[A-Za-z0-9_]+', text)

print("Hashtags:", result)