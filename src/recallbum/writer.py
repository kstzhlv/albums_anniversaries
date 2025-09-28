# standard
from datetime import datetime

# local
from .processor import match_albums_and_ratings


def write_albums_to_txt(username: str, threshold: int):
    content_to_write = match_albums_and_ratings(username, threshold)

    with open(".favourite_albums.txt", "w") as file:
        file.write(content_to_write)

    today = datetime.today()
    formatted_date = today.strftime("%B %-d, %Y")

    with open(".env", "w") as f:
        f.write(f"LAST_AOTY_PARSE={formatted_date}\n")


if __name__ == "__main__":
    write_albums_to_txt("codeling", 60)
