import re

def print_password(password) -> str:
    encrypted_password = password.group(2) + password.group(3) + password.group(4) + password.group(5)
    return f"Password: {encrypted_password}"

n = int(input())
regex = r'^(.+?)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$'

for _ in range(n):
    password = input()
    match = re.fullmatch(regex, password)
    if match:
        print(print_password(match))
    else:
        print("Try another password!")