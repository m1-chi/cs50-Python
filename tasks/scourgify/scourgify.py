import sys
import csv

def main():
    command_line_argument()
    students = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                new_name = row["name"].split(",")
                students.append({"first": new_name[1].lstrip(), "last": new_name[0], "house": row["house"]})
    except FileNotFoundError:
         sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in students:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


def command_line_argument():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv") == False and sys.argv[2].endswith(".csv") == False:
        sys.exit("Not a CSV file")



if __name__ == "__main__":
    main()