def factorial(first_number : int, second_number : int) -> float:
    first_factorial = first_number
    second_factorial = second_number
    for factor in range(1, first_number):
        first_factorial *= factor

    for factor in range(1, second_number):
        second_factorial *= factor

    result = first_factorial / second_factorial
    return result

first_number = int(input())
second_number = int(input())

print(f"{(factorial(first_number, second_number)):.2f}")