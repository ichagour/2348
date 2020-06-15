input_file = "inputDates.txt"
output_file = "parsedDates.txt"

map_of_months = {
    "April": 4,
    "December": 12,
    "May": 5,
    "March": 3,
    "October": 10,
    "November": 11,
    "January": 1,
    "February": 2,
    "August": 8,
    "July": 7,
    "June": 6,
    "September": 9,
}


def validate(raw_date):
    list = raw_date.split(" ")
    if len(list) != 3:
        return False
    month = list[0]
    if month not in map_of_months:
        return False
    day = list[1]
    if day[-1] != ",":
        return False
    return True


def is_end(raw_date):
    return raw_date == "-1\n"


def extract_month(raw_date):
    list = raw_date.split(" ")
    return map_of_months[list[0]]


def extract_day(raw_date):
    list = raw_date.split(" ")
    return list[1][0:-1]


def extract_year(raw_date):
    list = raw_date.split(" ")
    return list[2].strip()


with open(output_file, "w") as outfile, open(
    input_file, "r", encoding="utf-8"
) as infile:
    raw_dates = infile.readlines()
    for raw_date in raw_dates:
        if is_end(raw_date):
            break
        if validate(raw_date):
            month = extract_month(raw_date)
            day = extract_day(raw_date)
            year = extract_year(raw_date)
            date_str = f"{month}/{day}/{year}"
            print(date_str)
            outfile.write(date_str + "\n")









