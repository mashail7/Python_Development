sequence = list(map(int, input().split(", ")))
max_value = max(sequence)

for group in range(10, max_value + 10, 10):
    group_list = []

    for number in sequence:
        if group - 10 < number <= group:
            group_list.append(number)
            
    print(f"Group of {group}'s: {group_list}")