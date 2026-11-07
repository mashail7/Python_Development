encrypted_message = input()

command = input()
while command != "Decode":
    operation = command.split("|")
    first_command = operation[0]

    if first_command == "Move":
        number_of_moves = int(operation[1])
        first_letters = encrypted_message[:number_of_moves]
        second_letters = encrypted_message[number_of_moves:]
        encrypted_message = second_letters + first_letters
    elif first_command == "Insert":
        index = int(operation[1])
        value = operation[2]
        first_letters = encrypted_message[:index]
        second_letters = encrypted_message[index:]
        encrypted_message = first_letters + value + second_letters
    elif first_command == "ChangeAll":
        substring = operation[1]
        replacement = operation[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")