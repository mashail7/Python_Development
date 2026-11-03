import re

matches = []
line = input()
while line:
    pattern = "\d+"
    match = re.findall(pattern, line)
    matches += match
    line = input()
print(" ".join(matches))