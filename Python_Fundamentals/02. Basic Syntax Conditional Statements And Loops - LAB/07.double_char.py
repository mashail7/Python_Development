while True:
    string = input()
    if string == "End":
        break
    elif string == "SoftUni":
        continue

    new_string = ""

    for char in string:
        new_string += char
        new_string += char

    print(new_string)