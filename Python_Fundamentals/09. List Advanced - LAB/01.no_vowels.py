VOWELS = ['a', 'e', 'i', 'o', 'u']

word = input()
no_vowels_word = [char for char in word if char.lower() not in VOWELS]

print(''.join(no_vowels_word))