import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = Figlet(font=random.choice(fonts))
    out = f.renderText(input("Input: "))
    print("Output: ", out)
elif len(sys.argv) > 2:
    if sys.argv[-1] in fonts and sys.argv[-2] == "-f" or sys.argv[-2] == "--font":
        f = Figlet(font=sys.argv[-1])
        out2 = f.renderText(input("Input: "))
        print("Output: ",  out2)
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
