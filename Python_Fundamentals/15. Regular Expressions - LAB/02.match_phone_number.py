import re

text = input()
pattern = r'(?<!\S)\+359([ -])2\1\d{3}\1\d{4}\b'

matches = [match.group() for match in re.finditer(pattern, text)]
print(", ".join(matches))