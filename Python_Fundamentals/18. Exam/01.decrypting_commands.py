text = input()

while True:
    command = input()
    if command == "Finish":
        break

    tokens = command.split()
    if tokens[0] == "Replace":
        current_char = tokens[1]
        new_char = tokens[2]
        text = text.replace(current_char, new_char)
        print(text)
    elif tokens[0] == "Cut":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            first_string = text[:start_index]
            second_string = text[end_index + 1:]
            text = first_string + second_string
            print(text)
        else:
            print("Invalid indices!")
    elif tokens[0] == "Make":
        upper_or_lower = tokens[1]
        if upper_or_lower == "Upper":
            text = text.upper()
        elif upper_or_lower == "Lower":
            text = text.lower()
        print(text)
    elif tokens[0] == "Check":
        string_to_check = tokens[1]
        if string_to_check in text:
            print(f"Message contains {string_to_check}")
        else:
            print(f"Message doesn't contain {string_to_check}")
    elif tokens[0] == "Sum":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            sub_string = text[start_index:end_index + 1]
            ascii_string_code = 0
            for char in sub_string:
                ascii_string_code += ord(char)
            print(ascii_string_code)
        else:
            print("Invalid indices!")