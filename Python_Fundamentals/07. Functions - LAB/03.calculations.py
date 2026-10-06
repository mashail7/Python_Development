def calculate(operation, first_number, second_number):
    if operation == 'add':
        return first_number + second_number
    elif operation == 'subtract':
        return first_number - second_number
    elif operation == 'multiply':
        return first_number * second_number
    elif operation == 'divide':
        return first_number // second_number

operation = input()
first_number = int(input())
second_number = int(input())

result = calculate(operation, first_number, second_number)
print(result)