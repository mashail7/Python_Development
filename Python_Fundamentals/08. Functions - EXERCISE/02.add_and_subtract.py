def sum_numbers(first_number, second_number) -> int:
    return first_number + second_number

def subtract(summed_numbers, third_number) -> int:
    return summed_numbers - third_number

def add_and_subtract(first_number, second_number, third_number):
    summed_numbers = sum_numbers(first_number, second_number)
    return subtract(summed_numbers, third_number)

first_number = int(input())
second_number = int(input())
third_number = int(input())

result = add_and_subtract(first_number, second_number, third_number)
print(result)