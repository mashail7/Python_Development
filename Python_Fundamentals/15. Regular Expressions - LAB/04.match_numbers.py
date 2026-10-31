import re

text = input()
pattern = r'(?<!\S)-?(?:0|[1-9]\d*)(\.\d+)?(?!\S)'

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), end=' ')