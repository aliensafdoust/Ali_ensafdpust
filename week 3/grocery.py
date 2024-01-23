import sys

products = {}

while True:
    try:
        product = input().strip().upper()
        if not product in products:
            products.update({product: 1})
        elif product in products:
            products[product] += 1

    except EOFError:
        sorted_products = sorted(products)
        for product in sorted_products:
            print(products[product], product)
        sys.exit(0)
