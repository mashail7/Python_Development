def string_between_chars(first_character, second_character) -> list:
    characters = []
    for character in range(ord(first_character) + 1, ord(second_character)):
        characters.append(chr(character))
    return characters

first_character = input()
second_character = input()

result_as_list = string_between_chars(first_character, second_character)
print(" ".join(result_as_list))