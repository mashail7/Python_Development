divisor = int(input())
boundary = int(input())
largest_number = 1

for i in range(1, boundary + 1):
    if i % divisor == 0 and i > largest_number:
        largest_number = i

print(largest_number)