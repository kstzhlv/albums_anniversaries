import multiprocessing
import re

from .fetcher import fetch_page
from .web_parser import get_favourite_albums, get_rating_distribution, get_release_date

USER_PAGE_URL = "https://www.albumoftheyear.org/user/{}/"
BASE_URL = "https://www.albumoftheyear.org/user/{}/ratings/highest/{}/"


def count_pages_with_ratings_above_threshold(username: str, threshold: int) -> int:
    rating_distribution = get_rating_distribution(
        fetch_page(USER_PAGE_URL.format(username))
    )

    albums_higher_than_threshold = 0
    for rating, count in rating_distribution.items():
        if rating >= threshold:
            albums_higher_than_threshold += count

    # AOTY has 60 albums per page
    return int(albums_higher_than_threshold / 60) + 1


def process_page(args) -> str:
    username, page_number, threshold = args

    url = BASE_URL.format(username, page_number)
    html_content = fetch_page(url)
    artists, albums, ratings, hrefs = get_favourite_albums(html_content)

    content = ""

    for artist, album, rating, href in zip(artists, albums, ratings, hrefs):
        if rating >= threshold:
            html_content_for_album = fetch_page("https://www.albumoftheyear.org" + href)

            release_date = get_release_date(html_content_for_album).split("/")[0]
            release_date = re.sub(r"([a-zA-Z]+)(\d{1,2})", r"\1 \2", release_date)
            release_date = re.sub(r"(\d{1,2}),(\d{4})", r"\1, \2", release_date)

            print(f"got release date for {album}: {release_date}")

            content += f"{artist} - {album}: {release_date}\n"

    return content


def match_albums_and_ratings(username: str, threshold: int) -> str:
    number_of_pages = count_pages_with_ratings_above_threshold(username, threshold)

    with multiprocessing.Pool() as pool:
        args = [(username, page, threshold) for page in range(1, number_of_pages + 1)]
        results = pool.map(process_page, args)

    return "".join(results)
