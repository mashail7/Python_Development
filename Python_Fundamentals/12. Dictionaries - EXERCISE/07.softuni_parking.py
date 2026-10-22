n = int(input())
users = {}

for _ in range(n):
    command = input().split()
    action = command[0]
    user = command[1]
    if action == "register":
        license = command[2]

    if action == "register" and user not in users:
        users[user] = license
        print(f"{user} registered {license} successfully")
    elif action == "register" and user in users:
        print(f"ERROR: already registered with plate number {license}")

    if action == "unregister" and user in users:
        del users[user]
        print(f"{user} unregistered successfully")
    elif action == "unregister" and user not in users:
        print(f"ERROR: user {user} not found")

for user in users:
    print(f"{user} => {users[user]}")