items = input().split("|")
budget = int(input())
profit = 0
money_spent = 0
new_prices = []

for item in items:
    type_of_item, price = item.split('->')
    price = float(price)
    if type_of_item == 'Clothes' and price <= 50:
        if budget >= price:
            budget -= price
            money_spent += price
            profit += price * 0.40
            new_prices.append(price * 1.40)
    elif type_of_item == 'Shoes' and price <= 35:
        if budget >= price:
            budget -= price
            money_spent += price
            profit += price * 0.40
            new_prices.append(price * 1.40)
    elif type_of_item == 'Accessories' and price <= 20.50:
        if budget >= price:
            budget -= price
            money_spent += price
            profit += price * 0.40
            new_prices.append(price * 1.40)

for price in new_prices:
    print(f"{price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if 150 <= budget + money_spent + profit:
    print("Hello, France!")
else:
    print("Not enough money.")