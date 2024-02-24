import random


def main():
    level = get_level()
    i = 0
    right_score = 0
    while i < 10:
        i = i + 1
        random_num = generate_integer(level)
        name = ["x", "y"]
        dictionary = dict(zip(name, random_num))
        x = dictionary["x"]
        y = dictionary["y"]
        sum = x + y
        guess_count = 0
        guess_limit = 3
        while guess_count < guess_limit:
            guess_count += 1
            try:
                exc = int(input(f"{x} + {y} = "))
                if sum == exc:
                    right_score = right_score + 1
                    break
                else:
                    print("EEE")
                    continue
            except ValueError:
                print("EEE")
                pass
        else:
            guess_count = guess_limit
            print(f"{x} + {y} = {sum}")
    finalscore = right_score/10*10
    print(f"Score: {int(finalscore)}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return [random.randint(0, 9), random.randint(0, 9)]
    elif level == 2:
        return [random.randint(10, 99), random.randint(10, 99)]
    else:
        return [random.randint(100, 999), random.randint(100, 999)]




if __name__ == "__main__":
    main()