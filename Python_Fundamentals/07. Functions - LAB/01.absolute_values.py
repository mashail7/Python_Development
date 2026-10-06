def absolute_values(number):
    return abs(number)

input_list = input().split()
absolute_numbers = []

for number in input_list:
    absolute_number = absolute_values(float(number))
    absolute_numbers.append(absolute_number)

print(absolute_numbers)