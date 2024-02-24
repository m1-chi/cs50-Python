import re
import sys


def main():
    print(parse(input("HTML: ")))



def parse(s):
    url = re.findall(r'(?=src)src=\"(?P<src>[^\"]+)', s)
    url = " ".join(url)
    if matches := re.search(r"^(https?://)(www\.)?youtube\.com/embed/(.+)$", url):
        items = "https://youtu.be/",matches.group(3)
        short = ' '.join(items)
        short = short.replace(" ", "")
        return short




if __name__ == "__main__":
    main()