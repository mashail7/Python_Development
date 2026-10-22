products={}

while True:
    input_line = input()
    if input_line == 'buy':
        break

    arguments = input_line.split(' ')
    list_of_price_and_quantity =[]

    product = arguments[0]
    price = float(arguments[1])
    quantity = int(arguments[2])

    list_of_price_and_quantity.append(price)
    list_of_price_and_quantity.append(quantity)

    if product not in products:
        products[product] = list_of_price_and_quantity
    else:
        products[product][1] += list_of_price_and_quantity[1]
        products[product][0] = list_of_price_and_quantity[0]

for product,quantity_and_price_lst in products.items():
    print(f"{product} -> {quantity_and_price_lst[0] * quantity_and_price_lst[1]:.2f}")