n = int(input())
ascii_sum = 0

for i in range(n):
    ascii_code = ord(input())
    ascii_sum += ascii_code

print(f"The sum equals: {ascii_sum}")