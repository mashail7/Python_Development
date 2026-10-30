txt = input()
for index in range(len(txt)):
    if txt[index] == ":":
        print(txt[index] + txt[index + 1])