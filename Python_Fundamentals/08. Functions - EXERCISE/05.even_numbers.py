def list_of_even_numbers(sequence) -> list:
    even_numbers = []
    for number in sequence:
        number_as_integer = int(number)
        if number_as_integer % 2 == 0:
            even_numbers.append(number_as_integer)
    return even_numbers

sequence = input().split()

result_as_list = list_of_even_numbers(sequence)
print(result_as_list)