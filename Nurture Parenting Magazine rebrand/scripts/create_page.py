"""Creates a new WordPress page via REST API.
Usage: python3 create_page.py <title> <slug> <content_file>
"""
import sys
import json
import requests
from http.cookiejar import MozillaCookieJar

BASE = "https://www.nurtureparentingmagazine.com.au"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def main():
    title = sys.argv[1]
    slug = sys.argv[2]
    content_file = sys.argv[3]
    with open(content_file) as f:
        content = f.read()

    with open("/tmp/wp_nonce.txt") as f:
        nonce = f.read().strip()

    jar = MozillaCookieJar("/tmp/wp_cookies.txt")
    jar.load(ignore_discard=True, ignore_expires=True)

    session = requests.Session()
    session.cookies = jar
    session.headers.update({"User-Agent": UA, "X-WP-Nonce": nonce})

    resp = session.post(
        f"{BASE}/wp-json/wp/v2/pages",
        json={"title": title, "slug": slug, "content": content, "status": "publish"},
        timeout=60,
    )
    print("STATUS", resp.status_code)
    data = resp.json()
    print(json.dumps({k: data.get(k) for k in ("id", "link", "slug", "status")}, indent=2))
    if resp.status_code >= 400:
        print(json.dumps(data, indent=2)[:2000])


if __name__ == "__main__":
    main()
