txt = input()
encrypted_txt = ""

for letter in txt:
    new_letter = chr((ord(letter) + 3))
    encrypted_txt += new_letter

print(encrypted_txt)