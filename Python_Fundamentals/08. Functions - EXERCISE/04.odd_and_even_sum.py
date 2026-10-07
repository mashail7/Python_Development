def sum_all_even_and_odd_digits(number) -> str:
    even_sum = 0
    odd_sum = 0
    for digit in number:
        number_as_integer = int(digit)
        if number_as_integer % 2 == 0:
            even_sum += number_as_integer
        else:
            odd_sum += number_as_integer
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

number = input()

print(sum_all_even_and_odd_digits(number))