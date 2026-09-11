n = int(input())

for i in range(n):
    digit = int(input())
    if digit % 2 != 0:
        print(f"{digit} is odd!")
        break
    if i == n - 1:
        print("All numbers are even.")