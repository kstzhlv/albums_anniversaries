from bs4 import BeautifulSoup


def get_rating_distribution(html_content: str) -> dict[int, int]:
    soup = BeautifulSoup(html_content, "html.parser")
    rating_distribution = {}

    rating_rows = soup.select("#ratingDistribution .distRow")

    for row in rating_rows:
        label = row.select_one(".distLabel")
        count = row.select_one(".distCount")

        if label and count:
            # extract the rating and the count
            rating_distribution[int(label.text.strip().split("-")[0])] = int(count.text.strip())

    return rating_distribution


def get_favourite_albums(html_content: str) -> tuple[list[str], list[str], list[int], list[str]]:
    user_page = BeautifulSoup(html_content, "html.parser")

    artists = [artist.text.strip() for artist \
                in user_page.find_all("div", class_="artistTitle")]
    albums = [album.text.strip() for album \
                in user_page.find_all("div", class_="albumTitle")]
    ratings = [int(rating.text.strip()) for rating \
                in user_page.find_all("div", class_="rating") \
                if rating.text.strip().isdigit()]
    album_links = []

    for album_div in user_page.find_all("div", class_="albumTitle"):
        album_link = album_div.find_parent('a', href=True)
        if album_link:
            album_links.append(album_link.get('href'))
    
    return artists, albums, ratings, album_links

def get_release_date(html_content: str) -> str:
    album_page = BeautifulSoup(html_content, "html.parser")
    release_date_div = album_page.find("div", class_="detailRow")

    return release_date_div.get_text(strip=True)
