coffee = 0

while True:
    command = input()
    if command == "END":
        break

    command_to_lower = command.lower()

    if command_to_lower == "coding" or command_to_lower == "dog" or command_to_lower == "cat" or command_to_lower == "movie":
        if command.islower():
            coffee += 1
        elif command.isupper():
            coffee += 2

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)