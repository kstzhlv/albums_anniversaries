from processor import match_albums_and_ratings


def write_albums_to_txt(username: str, threshold: int):
    content_to_write = match_albums_and_ratings(username, threshold)

    with open(".favourite_albums.txt", "w") as file:
        file.write(content_to_write)


if __name__ == "__main__":
    write_albums_to_txt("codeling", 60)
