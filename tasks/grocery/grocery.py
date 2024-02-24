
shopping_list = []

while True:
    try:
        item = input("").casefold()
        shopping_list.append(item.upper())
        shopping_list.sort()
    except EOFError:
        print(end = "\n")
        numbers = {}
        for item in shopping_list:
            numbers[item] = shopping_list.count(item)
        for key, value in numbers.items():
            print(value, key)
        break

