strings = input().split()
total_sum = 0
first_string = strings[0]
second_string = strings[1]

if len(first_string) == len(second_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])

elif len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])

elif len(first_string) < len(second_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])

print(total_sum)