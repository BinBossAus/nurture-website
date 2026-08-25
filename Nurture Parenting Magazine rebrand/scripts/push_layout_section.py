"""Updates an Avada Theme Builder layout section (fusion_tb_section CPT) via the
classic wp-admin post.php form submission (no REST route exists for this CPT).
Usage: python3 push_layout_section.py <post_id> <content_file>
"""
import sys
import requests
from http.cookiejar import MozillaCookieJar

BASE = "https://www.nurtureparentingmagazine.com.au"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def main():
    post_id = sys.argv[1]
    content_file = sys.argv[2]
    with open(content_file) as f:
        content = f.read()

    jar = MozillaCookieJar("/tmp/wp_cookies.txt")
    jar.load(ignore_discard=True, ignore_expires=True)
    session = requests.Session()
    session.cookies = jar
    session.headers.update({"User-Agent": UA})

    edit_resp = session.get(f"{BASE}/wp-admin/post.php", params={"post": post_id, "action": "edit"})
    html = edit_resp.text

    import re

    def field(name, pattern=None):
        pat = pattern or rf'(?:id|name)=["\']{name}["\'][^>]*value=["\']([^"\']*)["\']'
        m = re.search(pat, html)
        return m.group(1) if m else None

    wpnonce = field("_wpnonce")
    referer = re.search(r'name="_wp_http_referer" value="([^"]*)"', html).group(1)
    post_author = field("post_author")
    post_type = field("post_type")
    original_post_status = field("original_post_status")
    post_title = field("original_post_title")
    meta_box_order_nonce = field("meta-box-order-nonce")
    closedpostboxes_nonce = field("closedpostboxesnonce")
    samplepermalink_nonce = field("samplepermalinknonce")

    print("nonce", wpnonce, "post_type", post_type, "title", post_title)

    data = {
        "_wpnonce": wpnonce,
        "_wp_http_referer": referer,
        "user_ID": "3",
        "action": "editpost",
        "originalaction": "editpost",
        "post_author": post_author,
        "post_type": post_type,
        "original_post_status": original_post_status,
        "referredby": "",
        "_wp_original_http_referer": "",
        "post_ID": post_id,
        "meta-box-order-nonce": meta_box_order_nonce,
        "closedpostboxesnonce": closedpostboxes_nonce,
        "samplepermalinknonce": samplepermalink_nonce,
        "post_title": post_title,
        "content": content,
        "post_status": "publish",
        "original_publish": "Update",
        "save": "Update",
    }

    resp = session.post(f"{BASE}/wp-admin/post.php", data=data, allow_redirects=False)
    print("STATUS", resp.status_code)
    print("LOCATION", resp.headers.get("Location"))


if __name__ == "__main__":
    main()
