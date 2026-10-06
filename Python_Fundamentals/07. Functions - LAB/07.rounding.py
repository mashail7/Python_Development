def rounding(number) -> int:
    return round(number)

input_list = input().split()
rounded_list = []

for number in input_list:
    rounded_number = rounding(float(number))
    rounded_list.append(rounded_number)

print(rounded_list)