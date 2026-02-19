
# INPUT_FILE = "products.json"

# # Load scraped JSON
# with open(INPUT_FILE, "r", encoding="utf-8") as f:
#     products = json.load(f)


import requests
from bs4 import BeautifulSoup
import json
import time

# --------------- CONFIG ----------------

CATEGORY_URL = "https://www.pinterest.com/search/pins/?q=mobile&rs=typed"
HEADERS = {"User-Agent": "Mozilla/5.0"}

OUTPUT_FILE = "images.json"
DELAY_BETWEEN_REQUESTS = 1
# ---------------------------------------



# Fetch category page
res = requests.get(CATEGORY_URL, headers=HEADERS)
soup = BeautifulSoup(res.text, "html.parser")

print(soup)
# 3️⃣ Sob img tag khuje src collect
img_tags = soup.find_all("img")
img_urls = [img.get("src") for img in img_tags if img.get("src")]

# 4️⃣ Print all src URLs
for url in img_urls:
    print(url)

# Save JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(img_urls, f, ensure_ascii=False, indent=4)

print(f"\n✅ Done! {len(img_urls)} products saved to {OUTPUT_FILE}")



