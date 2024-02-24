fraction = input("Fraction: ")
x, y = fraction.split("/")

if x >= y:
    result = round((int(x) / int(y)) * 100)
    print(result)