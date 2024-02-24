import re
import sys


def main():
    print(convert(input("Hours: ")))



def convert(s):
    if matches := re.search(r"^(\b([1-9]|1[0-2])\b(:[0-5]?[0-9])? (A|P)M) to (\b([1-9]|1[0-2])\b(:[0-5]?[0-9])? (A|P)M)$", s):
        start_work = matches.group(1)
        hour_start = matches.group(2)
        minutes_start = matches.group(3)

        end_work = matches.group(5)
        hour_end = matches.group(6)
        minutes_end = matches.group(7)

        if minutes_start == None:
            minutes_start = ":00"
        else:
            minutes_start = minutes_start

        if minutes_end == None:
            minutes_end = ":00"
        else:
            minutes_end = minutes_end

        if int(hour_start) < 10:
            hour_start = "{:02d}".format(int(hour_start))

        if int(hour_end) < 10:
            hour_end = "{:02d}".format(int(hour_end))


        if "PM" in start_work and "PM" in end_work:
            if int(hour_start) == 12:
                twentyfour_start = 12
            if int(hour_end) == 12:
                twentyfour_end = 12
            else:
                twentyfour_end = int(hour_end) + 12
                twentyfour_start = int(hour_start) + 12
            return f"{twentyfour_start}{minutes_start} to {twentyfour_end}{minutes_end}"

        elif "PM" in start_work and "AM" in end_work:
            if int(hour_start) == 12:
                twentyfour_start = 12
            else:
                twentyfour_start = int(hour_start) + 12

            if int(hour_end) == 12:
                twentyfour_end = "{:02d}".format(int(00))
            else:
                twentyfour_end = "{:02d}".format(int(hour_end))

            return f"{twentyfour_start}{minutes_start} to {twentyfour_end}{minutes_end}"

        elif "PM" in end_work and "AM" in start_work:
            if int(hour_end) == 12:
                twentyfour_end = 12
            else:
                twentyfour_end = int(hour_end) + 12

            if int(hour_start) == 12:
                twentyfour_start = "{:02d}".format(int(00))
            else:
                twentyfour_start = "{:02d}".format(int(hour_start))

            return f"{twentyfour_start}{minutes_start} to {twentyfour_end}{minutes_end}"

        else:
            return f"{hour_start}{minutes_start} to {hour_end}{minutes_end}"

    else:
        raise ValueError




if __name__ == "__main__":
    main()

