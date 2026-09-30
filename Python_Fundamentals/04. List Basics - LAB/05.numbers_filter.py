n = int(input())
numbers = []
filtered_list = []

for i in range(n):
    numbers.append(int(input()))

command = input()

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered_list.append(number)
elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered_list.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            filtered_list.append(number)
elif command == "positive":
    for number in numbers:
        if number >= 0:
            filtered_list.append(number)

print(filtered_list)