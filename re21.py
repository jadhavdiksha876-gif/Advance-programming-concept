import re

text = "<p>Hello!!!   Python,   Welcome.</p>"

text = re.sub(r'<[^>]*>', '', text)
text = re.sub(r'[^\w\s]', '', text)
text = re.sub(r'\s+', ' ', text).strip()

print(text)