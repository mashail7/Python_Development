n = int(input())
word = input()
my_list = []
filtered_list = []

for _ in range(n):
    string = input()
    my_list.append(string)

    if word in string:
        filtered_list.append(string)

print(my_list)
print(filtered_list)