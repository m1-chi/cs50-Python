import datetime
from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    get_birthdate()

def get_birthdate():
    birthdate = input("Date of Birth: ")
    return calculate(birthdate)

def calculate(birthdate):

    try:
        birth = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
    except ValueError:
        sys.exit("Invalid date")

    diff = date.today() - birth.date()
    minutes = diff.days*1440
    result = p.number_to_words(minutes, andword = '').capitalize()
    print(result + " minutes")
    return result + " minutes"




if __name__ == "__main__":
    main()