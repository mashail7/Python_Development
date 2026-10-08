CAPACITY = 255

n = int(input())
liters = 0

for i in range(n):
    liters_to_add = int(input())
    if liters_to_add + liters > CAPACITY:
        print("Insufficient capacity!")
    else:
        liters += liters_to_add

print(liters)