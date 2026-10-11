def found_indices (numbers_list: list) -> list:
    even_indices = [index for index in range(len(numbers_list)) if numbers_list[index] % 2 == 0]
    return even_indices


numbers_list = list(map(int,input().split(", ")))

print(found_indices(numbers_list))