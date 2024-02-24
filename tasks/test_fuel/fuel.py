def main():
    fraction = input("Fraction: ")
    value = convert(fraction)
    percentage = gauge(value)
    print(percentage)



def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            result = x / y
            if result <= 1:
                percent = int(result * 100)
                return percent
            else:
                pass
        except (ValueError, ZeroDivisionError):
            raise



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()




