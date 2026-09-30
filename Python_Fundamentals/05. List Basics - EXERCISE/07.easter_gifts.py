gifts_list = input().split()

while True:
    command = input().split()
    if command == ["No", "Money"]:
        break

    if command[0] == 'OutOfStock':
        gift = command[1]
        while gift in gifts_list:
            gift_index = gifts_list.index(gift)
            gifts_list.pop(gift_index)
            gifts_list.insert(gift_index, 'None')
    elif command[0] == "Required":
        gift = command[1]
        index = int(command[2])
        if 0 <= index < len(gifts_list):
                gifts_list[index] = gift

    elif command[0] == 'JustInCase':
        gift = command[1]
        gifts_list.pop()
        gifts_list.append(gift)

for gift in gifts_list:
    if gift != 'None':
        print(f"{gift} ", end='')