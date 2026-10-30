text = input()
strength = 0
result = ""

for i in range(len(text)):
    char = text[i]

    if char == ">":
        result += char
        strength += int(text[i + 1])
    elif strength > 0:
        strength -= 1
    else:
        result += char

print(result)