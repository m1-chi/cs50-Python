import inflect
p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        if len(names) == 1:
            print(f"\nAdieu, adieu, to {name}")
        elif len(names) >= 2:
            names = p.join((names))
            print(f"\nAdieu, adieu, to {names}")
        break
