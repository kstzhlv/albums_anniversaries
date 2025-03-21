import subprocess
from datetime import datetime
import time


def send_notification():
    TITLE = "Album anniversary!"
    albums_anniversaries = {}

    today = datetime.today()
    formatted_date = today.strftime("%B %d, %Y")
    print(formatted_date)

    with open(".favourite_albums.txt", "r") as file:
        for line in file:
            date_and_year = formatted_date.split(", ")
            if date_and_year[0] in line:
                albums_anniversaries[line.split(":")[0]] = int(date_and_year[1]) - int(line.split(", ")[-1])

    for album, years_since_release in albums_anniversaries.items():
        if years_since_release > 1:
            message = f"{album} is turning {years_since_release} years old today!"
        else:
            message = f"{album} is turning {years_since_release} year old today!"

        subprocess.run(["notify-send", TITLE, message])
        time.sleep(1)
        
send_notification()