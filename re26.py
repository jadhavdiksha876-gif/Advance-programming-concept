import re

text = """
Research paper DOI: 10.1234/abcd.5678
Published in 2024.
Email: author@example.com
URL: https://example.com/paper
"""

doi = re.findall(r'\b10\.\d{4,9}/[^\s]+', text)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.[A-Za-z]{2,}\b', text)
urls = re.findall(r'https?://[^\s]+', text)

print("DOI:", doi)
print("Publication years:", years)
print("Email addresses:", emails)
print("URLs:", urls)