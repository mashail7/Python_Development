sequences = input().split()
total_result = 0

for sequence in sequences:
    first_letter = ""
    number = ""
    second_letter = ""
    for letter in sequence:
        if letter.isalpha():
            if first_letter == "":
                first_letter += letter
            else:
                second_letter += letter
        elif letter.isdigit():
            number += letter

    if first_letter.upper() == first_letter:
        letter_number = ord(first_letter.lower()) - ord("a") + 1
        number = int(number) / letter_number
    else:
        letter_number = ord(first_letter) - ord("a") + 1
        number = int(number) * letter_number

    if second_letter.upper() == second_letter:
        letter_number = ord(second_letter.lower()) - ord("a") + 1
        number -= letter_number
    else:
        letter_number = ord(second_letter) - ord("a") + 1
        number += letter_number

    total_result += number

print(f"{total_result:.2f}")