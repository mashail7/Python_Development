def decode_first_letter(word: str) -> str:
    code = ""
    for letter in word:
        if letter.isdigit():
            code += letter
        else:
            break
    first_letter = chr(int(code))
    word = word.replace(code, first_letter)
    return word

def replace_first_letter(word: str) -> str:
    word = list(word)
    word[1], word[-1] = word[-1], word[1]
    word = "".join(word)
    return word

secret_message = input().split()
deciphered_message = []

for word in secret_message:
    word = decode_first_letter(word)
    word = replace_first_letter(word)

    deciphered_message.append(word)

print(" ".join(deciphered_message))