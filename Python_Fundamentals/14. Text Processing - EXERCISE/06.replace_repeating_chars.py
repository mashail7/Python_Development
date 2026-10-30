string = input()
new_string = string[0]
for letter in string:

    if letter != new_string[-1]:
        new_string += letter

print(new_string)