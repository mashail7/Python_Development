numbers_string = input().split()
numbers_list = []
smallest_number = 0
biggest_number = 0
sum_of_numbers = 0

for number in numbers_string:
    number_integer = int(number)
    numbers_list.append(number_integer)

smallest_number = min(numbers_list)
biggest_number = max(numbers_list)
sum_of_numbers = sum(numbers_list)

print(f"The minimum number is {smallest_number}")
print(f"The maximum number is {biggest_number}")
print(f"The sum number is: {sum_of_numbers}")