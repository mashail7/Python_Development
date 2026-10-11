notes = []

while True:
    command = input()
    if command == 'End':
        break

    importance, note = command.split('-')

    notes.append((int(importance), note))

notes.sort()

result = [note[1] for note in notes]
print(result)