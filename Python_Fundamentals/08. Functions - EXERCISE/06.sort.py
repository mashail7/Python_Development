def sort_numbers(sequence) -> list:
    sorted_numbers = []
    for number in sequence:
        sorted_numbers.append(int(number))
        sorted_numbers.sort()
    return sorted_numbers

sequence = input().split()

result_as_list = sort_numbers(sequence)
print(result_as_list)