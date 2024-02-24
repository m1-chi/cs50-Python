print("Amount Due: 50")
x = 50

while True:
    coins = int(input("Insert Coin: "))
    if coins <= 50 and coins in (25, 10, 5):
        x = x - coins
        if x > 0:
            print(f"Amount Due: {x}")
        if x == 0:
            print(f"Change Owed: {x}")
            break
        if x < 0:
            print(f"Change Owed: {(x * -1)}")
            break
    else:
        print("Amount Due: 50")


