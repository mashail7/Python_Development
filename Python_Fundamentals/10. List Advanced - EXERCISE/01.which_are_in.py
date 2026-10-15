substrings =  input().split(", ")
strings = input().split(", ")

new_list = []
for substring in substrings:
    for string in strings:
        if substring in string:
            new_list.append(substring)
            break
print(new_list)