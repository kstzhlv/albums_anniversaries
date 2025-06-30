import time
from datetime import datetime


def remind():
    TITLE = "Album anniversary!"
    albums_anniversaries = {}
    albums_anniversaries_in_month = {}

    today = datetime.today()
    formatted_date = today.strftime("%B %-d, %Y")
    print(formatted_date)

    month = formatted_date.split(" ")[0]
    year = formatted_date[-4:]
    date = formatted_date.split(", ")[0]

    with open(".favourite_albums.txt", "r") as file:
        for line in file:
            line_split_by_colon = line.split(": ")
            if f"{date}, " in line:
                albums_anniversaries[line_split_by_colon[0]] = int(year) - int(
                    line.split(", ")[-1]
                )

            else:
                if (month in line) and (len(line_split_by_colon[1].split(",")) == 1):
                    albums_anniversaries_in_month[line_split_by_colon[0]] = int(
                        year
                    ) - int(line[-5:])

    for album, years_since_release in albums_anniversaries.items():
        if years_since_release > 1:
            message = f"{album} is turning {years_since_release} years old today!"
        else:
            message = f"{album} is turning {years_since_release} year old today!"

        print(TITLE, message)
        time.sleep(1)

    for album, years_since_release in albums_anniversaries_in_month.items():
        if years_since_release > 1:
            message = (
                f"{album} was released in this month {years_since_release} years ago!"
            )
        else:
            message = (
                f"{album} was released in this month {years_since_release} a year ago!"
            )

        print(TITLE, message)
        time.sleep(1)
