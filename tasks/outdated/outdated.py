months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
             month, day, year = date.split("/")
             if int(month) <= 12 and int(day) <= 31:
                print(f"{year}-{int(month):02d}-{int(day):02}")
                break
        elif "," in date:
            month, day, year = date.split()
            day = day.replace(",", "")
            if month in months and int(day) <= 31:
                print(f"{year}-{months[month]}-{int(day):02}")
                break
        else:
            pass
    except ValueError:
        pass

