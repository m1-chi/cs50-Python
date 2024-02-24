import sys
from PIL import Image
import os
import PIL

def main():
    command_line_argument()
    command_line_argument_same()
    try:
        input = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit()
    size = shirt.size
    resize_image = PIL.ImageOps.fit(input, size)
    resize_image.paste(shirt, mask = shirt)
    resize_image.save(sys.argv[2])


def command_line_argument():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def command_line_argument_same():
     input_ext = os.path.splitext(sys.argv[1])
     output_ext = os.path.splitext(sys.argv[2])
     if sys.argv[1].endswith((".png", ".jpg", ".jpeg")) and sys.argv[2].endswith((".png", ".jpg", ".jpeg")):
        if input_ext[1] != output_ext[1]:
            sys.exit("Input and output have different extensions")
        if '' in input_ext and '' in output_ext:
            sys.exit("Invalid input")
     else:
        sys.exit("Invalid input")



if __name__ == "__main__":
    main()