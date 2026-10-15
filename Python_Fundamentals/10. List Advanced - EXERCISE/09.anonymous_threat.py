input_list = input().split()

while True:
    command = input().split()

    if command[0] == "3:1":
        break

    elif command[0] == "merge":
        start = int(command[1])
        end = int(command[2])

        start = max(0, start)
        end = min(len(input_list) - 1, end)

        if start <= end:
            merged = "".join(input_list[start:end + 1])
            input_list[start:end + 1] = [merged]

    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])

        element = input_list[index]
        partition_length = len(element) // partitions

        parts = []

        for i in range(partitions - 1):
            start = i * partition_length
            end = start + partition_length
            parts.append(element[start:end])

        parts.append(element[(partitions - 1) * partition_length:])

        input_list[index:index + 1] = parts

print(" ".join(input_list))