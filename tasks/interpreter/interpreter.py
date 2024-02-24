expression = input("Expression: ")
x, y, z = expression.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
else:
    d = float(x) / float(z)
    print(("{:.1f}".format(d)))
