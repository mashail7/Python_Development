def check_if_palindrome(number) -> bool:
    reversed_number = number[::-1]
    if number == reversed_number:
        return True
    return False

numbers_list = input().split(", ")

for number in numbers_list:
    print(check_if_palindrome(number))