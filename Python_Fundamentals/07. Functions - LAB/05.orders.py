def calculate_price(order, quantity):
    if order == "coffee":
        return 1.50 * quantity
    elif order == "water":
        return 1.00 * quantity
    elif order == "coke":
        return 1.40 * quantity
    elif order == "snacks":
        return 2.00 * quantity

order = input()
quantity = int(input())

result = calculate_price(order, quantity)
print(f"{result:0.2f}")