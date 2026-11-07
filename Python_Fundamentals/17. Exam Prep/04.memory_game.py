sequence = input().split()
number_of_moves_until_now = 0

while True:
    command = input()
    if command == "end":
        print(f"Sorry you lose :(")
        print(" ".join(sequence))
        break

    integers = command.split()
    first_int = int(integers[0])
    second_int = int(integers[1])
    number_of_moves_until_now += 1

    if first_int == second_int or first_int < 0 or second_int < 0 or first_int >= len(sequence) or second_int >= len(sequence):
        error_number = f"-{number_of_moves_until_now}a"
        index_to_insert = len(sequence) // 2
        sequence.insert(index_to_insert, error_number)
        sequence.insert(index_to_insert, error_number)
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence[first_int] == sequence[second_int]:
            print(f"Congrats! You have found matching elements - {sequence[first_int]}!")
            sequence.pop(max(first_int, second_int))
            sequence.pop(min(first_int, second_int))
        else:
            print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {number_of_moves_until_now} turns!")
        break