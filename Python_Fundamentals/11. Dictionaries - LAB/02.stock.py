elements = input().split()
products = {}

for i in range(0, len(elements), 2):
    products[elements[i]] = elements[i+1]

products_to_check = input().split()
for product in products_to_check:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")