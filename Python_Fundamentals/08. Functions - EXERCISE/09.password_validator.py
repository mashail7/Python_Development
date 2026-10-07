def validate_password(password) -> list:
    commands = []

    check_length_is_valid = check_length(password)
    if check_length_is_valid:
        commands.append(check_length_is_valid)

    check_letters_digits_is_valid = check_letters_digits(password)
    if check_letters_digits_is_valid:
        commands.append(check_letters_digits_is_valid)

    check_two_digits_is_valid = check_two_digits(password)
    if check_two_digits_is_valid:
        commands.append(check_two_digits_is_valid)

    return commands

def check_length(password) -> str:
    if 6 <= len(password) <= 10:
        return None
    return "Password must be between 6 and 10 characters"

def check_letters_digits(password) -> str:
    if password.isalnum():
        return None
    return "Password must consist only of letters and digits"

def check_two_digits(password) -> str:
    counter = 0
    for char in password:
        if char.isdigit():
            counter += 1
    if counter >= 2:
        return None
    return "Password must have at least 2 digits"

password = input()

is_valid = validate_password(password)
if is_valid:
    print("\n".join(is_valid))
else:
    print("Password is valid")