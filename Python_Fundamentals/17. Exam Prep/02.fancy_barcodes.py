import re

n = int(input())
pattern = r'^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$'

for barcodes in range(n):
    barcode = input()

    match = re.match(pattern, barcode)
    if match:
        product_group = ""
        for digit in barcode:
            if digit.isdigit():
                product_group += digit
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")