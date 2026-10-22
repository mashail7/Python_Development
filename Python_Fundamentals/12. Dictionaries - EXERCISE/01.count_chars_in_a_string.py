characters = input()
letters = {}
for character in characters:
    if character == " ":
        continue
    if character not in letters.keys():  # if character not in letters
        letters[character] = 0
    letters[character] += 1
for char, occurences in letters.items():
    print(f"{char} -> {occurences}")