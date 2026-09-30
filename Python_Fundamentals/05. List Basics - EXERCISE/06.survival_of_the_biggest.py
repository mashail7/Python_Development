import sys

input_list = list(map(int, input().split()))
n = int(input())

for i in range(n):
    smallest_number = sys.maxsize

    for j in range(len(input_list)):
        number = int(input_list[j])
        if number < smallest_number:
            smallest_number = number

    input_list.remove(smallest_number)

print(", ".join(map(str, input_list)))