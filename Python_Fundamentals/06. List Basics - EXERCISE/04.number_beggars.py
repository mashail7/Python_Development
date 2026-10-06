my_list = input().split(", ")
count_beggars = int(input())
sum_list = []

start_index = 0

while start_index < count_beggars:
    sum_for_beggar = 0
    for i in range(start_index, len(my_list), count_beggars):
        sum_for_beggar += int(my_list[i])

    sum_list.append(sum_for_beggar)
    start_index += 1
    sum_for_beggar = 0

print(sum_list)