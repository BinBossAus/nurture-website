import re
import requests
from http.cookiejar import MozillaCookieJar

BASE = "https://www.nurtureparentingmagazine.com.au"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

jar = MozillaCookieJar("/tmp/wp_cookies.txt")
jar.load(ignore_discard=True, ignore_expires=True)
s = requests.Session()
s.cookies = jar
s.headers.update({"User-Agent": UA})

r = s.get(f"{BASE}/wp-admin/themes.php", params={"page": "avada_options"})
html = r.text
idx = html.find("option_page")
chunk = html[max(0, idx - 2000):idx + 200]
m = re.search(r'name=._wpnonce.\s+value=.([a-f0-9]+).', chunk)
if not m:
    m = re.search(r'_wpnonce[^a-f0-9]{1,20}([a-f0-9]{10})', chunk)
nonce = m.group(1)
print("nonce", nonce)

with open("/tmp/options_go_live.json") as f:
    payload = f.read()

s.headers.update({"Referer": f"{BASE}/wp-admin/themes.php?page=avada_options"})
resp = s.post(
    f"{BASE}/wp-admin/options.php",
    data={
        "option_page": "fusion_options_group",
        "action": "update",
        "_wpnonce": nonce,
        "_wp_http_referer": "/wp-admin/themes.php?page=avada_options",
        "fusion_options[import_code]": payload,
        "import": "Import",
    },
    allow_redirects=False,
)
print("STATUS", resp.status_code)
print("LOCATION", resp.headers.get("Location"))
if resp.status_code == 403:
    print(resp.text[:2000])
