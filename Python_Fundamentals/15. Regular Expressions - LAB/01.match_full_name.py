import re

names = input()
pattern = r'\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b'

matches = re.findall(pattern, names)
print(" ".join(matches))