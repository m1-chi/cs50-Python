menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

menu = {k.casefold(): v for k, v in menu.items()}

total = 0

while True:
    try:
        item = input("Item: ").casefold()
        for food in menu:
            if item == food:
                total = total + menu[food]
                print(f"Total: ${total:.2f}", end = "\n")
    except EOFError:
       print(end = "\n")
       break







