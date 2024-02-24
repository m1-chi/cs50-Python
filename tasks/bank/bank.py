def main():
    greeting = input("Please enter a greeting: ").strip()
    money = value(greeting)
    print(f"${money}")

def value(greeting):
    if greeting.startswith("hello".casefold()):
        return 0
    elif greeting.startswith("h".casefold()):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()