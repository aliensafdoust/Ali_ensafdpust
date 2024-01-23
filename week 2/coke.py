price = 50
coins = 0
while True:
    if price <= 0:
        break

    print(f"Amount Due: {price}")
    Insert_coin = int(input("Insert Coin: "))
    if Insert_coin == 5 or Insert_coin == 10 or Insert_coin == 25:
        if Insert_coin <= price:
            price = price - Insert_coin
            continue
        elif Insert_coin > price:
            coins = Insert_coin - price
            price = 0
            continue

price += coins
print(f"Change Owed: {price}")
