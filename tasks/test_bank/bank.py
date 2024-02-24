def main():
    greeting = input("Please enter a greeting: ").casefold().strip()
    money = value(greeting)
    print(f"${money}")

def value(greeting):
    if greeting.startswith("hello") or greeting.startswith("Hello"):
        return 0
    elif greeting.startswith("h") or greeting.startswith("Hi"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()