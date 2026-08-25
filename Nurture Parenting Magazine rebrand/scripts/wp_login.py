# -*- coding: utf-8 -*-
"""Logs into the Nurture WordPress site using NURTURE_WP_URL / NURTURE_WP_USERNAME /
NURTURE_WP_PASSWORD env vars, and saves the session cookies + a REST nonce to disk
so that push_page.py (and similar scripts) can reuse them.

Usage: python3 wp_login.py
Writes: /tmp/wp_cookies.txt (Netscape cookie jar), /tmp/wp_nonce.txt
"""
import os
import re
import sys
import requests
from http.cookiejar import MozillaCookieJar

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def main():
    wp_url = os.environ.get("NURTURE_WP_URL", "").rstrip("/")
    username = os.environ["NURTURE_WP_USERNAME"]
    password = os.environ["NURTURE_WP_PASSWORD"]

    # NURTURE_WP_URL points at the wp-admin URL (redirects to wp-login.php when
    # logged out); derive the site base URL from it.
    base = re.sub(r"/wp-admin/?$", "", wp_url) or "https://www.nurtureparentingmagazine.com.au"

    session = requests.Session()
    session.headers.update({"User-Agent": UA})

    session.get(f"{base}/wp-login.php")

    resp = session.post(
        f"{base}/wp-login.php",
        data={
            "log": username,
            "pwd": password,
            "wp-submit": "Log In",
            "redirect_to": f"{base}/wp-admin/",
            "testcookie": "1",
        },
        allow_redirects=True,
    )

    if "wp-admin" not in resp.url or "loggedout" in resp.url:
        print("LOGIN FAILED", resp.url, file=sys.stderr)
        sys.exit(1)

    m = re.search(r'wpApiSettings = \{.*?"nonce":"([a-f0-9]+)"', resp.text)
    if not m:
        print("Could not find REST nonce on dashboard page", file=sys.stderr)
        sys.exit(1)
    nonce = m.group(1)

    jar = MozillaCookieJar("/tmp/wp_cookies.txt")
    for c in session.cookies:
        jar.set_cookie(c)
    jar.save(ignore_discard=True, ignore_expires=True)

    with open("/tmp/wp_nonce.txt", "w") as f:
        f.write(nonce)

    print("Login OK. Nonce:", nonce)


if __name__ == "__main__":
    main()
