def main():
    twitter = input("Input: ")
    print(f"Output: {shorten(twitter)}")

vowels = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U")

def shorten(word):
    for character in word:
        if character in vowels:
            word = word.replace(character, "").
    return word


if __name__ == "__main__":
    main()
