months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        Date = input("Date: ").strip()
        #type 1
        if "/" in Date:
            month , day , year = Date.split("/")
        #type 2
        elif "," in Date:
            month_day , year = Date.split(",")
            month , day = month_day.strip().split(" ")

            if month in months :
                month = (months.index(month)) + 1
            else:
                raise ValueError
        else :
            raise ValueError
        if int(day) > 31 or int(month) > 12:
            raise ValueError

    except (ValueError, EOFError):
        pass

    else:
        print(f"{int(year)}-{int(month):02}-{int(day):02}")
        break


