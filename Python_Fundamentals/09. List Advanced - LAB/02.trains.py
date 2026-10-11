number_wagons = int(input())
train = [0] * number_wagons

while True:
    command = input()
    if command == "End":
        break

    command = command.split()

    if command[0] == "add":
        train[-1] += int(command[1])
    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        train[index] -= people

print(train)