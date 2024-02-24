question_life = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().strip()


if question_life == "42" or question_life == "forty-two" or question_life == "forty two":
    print("Yes")
else:
    print("No")