from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import chardet


HEADERS = {"User-Agent": "Mozilla/6.0"}

def fetch_page(url: str) -> str:
    try:
        request = Request(url, headers=HEADERS)
        page = urlopen(request).read()
        encoding = chardet.detect(page)["encoding"]
    except (URLError, HTTPError) as e:
        raise Exception(f"Failed to fetch page: {e}")
    
    return page.decode(encoding, errors="replace")