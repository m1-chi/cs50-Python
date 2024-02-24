import re
import sys



def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.match(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip):
        parts = ip.split(".")
        for i in parts:
            if int(i) > 255 or int(i) < 0:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()