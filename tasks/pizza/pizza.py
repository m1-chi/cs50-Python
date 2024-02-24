import sys
import csv
from tabulate import tabulate


if len(sys.argv) == 2:
    file_name = sys.argv[1]
    if file_name.endswith(".csv"):
        try:
            table = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    table.append(row)
                headers = table[0]
                table = table[1:]
                print(tabulate(table, headers, tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
         sys.exit("Not a CSV file")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")
