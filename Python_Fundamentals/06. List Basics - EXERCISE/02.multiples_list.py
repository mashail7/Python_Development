factor = int(input())
length = int(input())
my_list = []

for number in range(1, length + 1):
    new_number = factor * number
    my_list.append(new_number)

print(my_list)