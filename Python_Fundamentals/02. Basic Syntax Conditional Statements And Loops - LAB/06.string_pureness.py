n = int(input())

for i in range(1, n + 1):
    n_string = input()
    flag = False

    for char in n_string:
        if char == ',' or char == '.' or char == '_':
            flag = True
            break

    if not flag:
        print(f"{n_string} is pure.")
    else:
        print(f"{n_string} is not pure!")