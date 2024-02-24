import sys
import csv


if len(sys.argv) == 2:
    file_name = sys.argv[1]
    if file_name.endswith(".py"):
        try:
            lines = []
            with open(sys.argv[1], "r") as file:
                for line in file.readlines():
                    line = line.rstrip().lstrip()
                    if line.startswith("#") == False and line !='':
                        lines.append(line)
                print(len(lines))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
         sys.exit("Not a Python file")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")



