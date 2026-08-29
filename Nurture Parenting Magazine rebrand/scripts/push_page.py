"""Pushes generated Fusion Builder shortcode content to a WordPress page via the
REST API, using the session saved by wp_login.py.

Usage: python3 push_page.py <page_id> <content_file>
"""
import sys
import json
import requests
from http.cookiejar import MozillaCookieJar

BASE = "https://www.nurtureparentingmagazine.com.au"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def main():
    page_id = sys.argv[1]
    content_file = sys.argv[2]
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
        f"{BASE}/wp-json/wp/v2/pages/{page_id}",
        json={"content": content},
        timeout=60,
    )
    print("STATUS", resp.status_code)
    try:
        data = resp.json()
        print("id", data.get("id"), "link", data.get("link"), "modified", data.get("modified"))
        if resp.status_code >= 400:
            print(json.dumps(data, indent=2)[:2000])
    except Exception as e:
        print("parse error", e, resp.text[:2000])


if __name__ == "__main__":
    main()
