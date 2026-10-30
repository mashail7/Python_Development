string = input()
raged_string = ""
sequence_to_repeat = ""
number = ""
unique_symbols = set()

for char in string:
    if char.isdigit():
        number += char
    else:
        if number:
            raged_string += sequence_to_repeat.upper() * int(number)
            sequence_to_repeat = ""
            number = ""

        sequence_to_repeat += char
        unique_symbols.add(char.upper())

raged_string += sequence_to_repeat.upper() * int(number)

print(f"Unique symbols used: {len(unique_symbols)}")
print(raged_string)
