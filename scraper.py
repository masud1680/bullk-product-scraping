# import requests
# from bs4 import BeautifulSoup
# import json
# import time

# # --------------- CONFIG ----------------
# CATEGORY_URL = "https://chocolateshopbd.com/product-category/chocolate/feastables/"
# HEADERS = {"User-Agent": "Mozilla/5.0"}
# OUTPUT_FILE = "products.json"
# DELAY_BETWEEN_REQUESTS = 1  # seconds
# # ---------------------------------------

# all_products = []

# # Fetch category page
# res = requests.get(CATEGORY_URL, headers=HEADERS)
# soup = BeautifulSoup(res.text, "html.parser")

# # print(f'{soup}')

# # Select all product cards (adjust selector)
# product_cards = soup.select("a.product-image-link")  # usually link to detail page

# print(f"Found {len(product_cards)} products on this page.")

# for idx, card in enumerate(product_cards, start=1):
#     product_url = card["href"]
#     print(f"{idx}. Scraping product: {product_url}")

#     try:
#         # Visit product detail page
#         r = requests.get(product_url, headers=HEADERS)
#         s = BeautifulSoup(r.text, "html.parser")

#         # Extract product details (adjust selectors according to your site)
#         title_tag = s.find("h1", class_="product_title")
#         price_tag = s.find("span", class_="price")
#         desc_tag = s.find("div", class_="description")
#         image_tag = s.find("img", class_="wp-post-image")

#         title = title_tag.text.strip() if title_tag else ""
#         price = price_tag.text.strip().replace("$", "") if price_tag else ""
#         description = desc_tag.text.strip() if desc_tag else ""
#         image_url = image_tag["src"] if image_tag else ""

#         product_data = {
#             "title": title,
#             "price": price,
#             "description": description,
#             "image_url": image_url,
#             "source_url": product_url
#         }

#         all_products.append(product_data)
#         time.sleep(DELAY_BETWEEN_REQUESTS)

#     except Exception as e:
#         print("❌ Error scraping product:", e)
#         continue

# # Save to JSON
# with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
#     json.dump(all_products, f, ensure_ascii=False, indent=4)

# print(f"\n✅ Done! {len(all_products)} products saved to {OUTPUT_FILE}")





# ==========================================
# single page one product images extract
# ==========================================



import requests
from bs4 import BeautifulSoup
import json
import time

# --------------- CONFIG ----------------
# CATEGORY_URL = "https://chocolateshopbd.com/product-category/chocolate/hersheys/"
CATEGORY_URL = "https://chocolateshopbd.com/product-category/chocolate/feastables/"
HEADERS = {"User-Agent": "Mozilla/5.0"}
OUTPUT_FILE = "products.json"
DELAY_BETWEEN_REQUESTS = 1
# ---------------------------------------

all_products = []

# Fetch category page
res = requests.get(CATEGORY_URL, headers=HEADERS)
soup = BeautifulSoup(res.text, "html.parser")

# Select all product cards
product_cards = soup.select("a.product-image-link")  # adjust selector

print(f"Found {len(product_cards)} products on this page.")

for idx, card in enumerate(product_cards, start=1):
    product_url = card["href"]
    print(f"{idx}. Scraping product: {product_url}")

    try:
        r = requests.get(product_url, headers=HEADERS)
        s = BeautifulSoup(r.text, "html.parser")

        # ---- Extract title, description, image ----
        title_tag = s.find("h1", class_="product_title")
        desc_tag = s.find("div", class_="woocommerce-Tabs-panel--description")
        image_tag = s.find("img", class_="wp-post-image")

        title = title_tag.text.strip() if title_tag else ""
        description = desc_tag.text.strip() if desc_tag else ""
        image_url = image_tag["src"] if image_tag else ""

        # ---- Extract prices ----
        # del_tag = s.find("del")   # original price
        # ins_tag = s.find("ins")   # current price
        
            
       

        # def extract_price(tag):
        #     if tag:
        #         bdi = tag.find("bdi")
        #         if bdi:
        #             price_text = bdi.get_text().replace("৳","").replace(",","").strip()
        #             try:
        #                 return int(float(price_text))
        #             except:
        #                 return 0
        #     return 0

        # original_price = extract_price(del_tag)
        # current_price = extract_price(ins_tag)




        price_box = s.find("p", class_="price")

        original_price = 0
        current_price = 0

        if price_box:

            # Case 1: Discounted product (has del + ins)
            del_tag = price_box.find("del")
            ins_tag = price_box.find("ins")

            def extract_price_from_tag(tag):
                if tag:
                    bdi = tag.find("bdi")
                    if bdi:
                        price_text = bdi.get_text().replace("৳", "").replace(",", "").strip()
                        return int(float(price_text))
                return 0

            if del_tag and ins_tag:
                original_price = extract_price_from_tag(del_tag)
                current_price = extract_price_from_tag(ins_tag)

            # Case 2: No discount (single price)
            else:
                bdi = price_box.find("bdi")
                if bdi:
                    price_text = bdi.get_text().replace("৳", "").replace(",", "").strip()
                    current_price = int(float(price_text))
                    original_price = float(price_text) + (float(price_text) * 25  / 100)



        # ---- Prepare product dict ----
        product_data = {
            "category_id": 2,
            "sub_category_id": 5,
            "title": title,
            "purches_price": (current_price * 75 ) / 100,
            "current_price": current_price,
            "original_price": original_price,
            "description": description,
            "image_url": image_url,
            "source_url": product_url
        }

        all_products.append(product_data)
        time.sleep(DELAY_BETWEEN_REQUESTS)

    except Exception as e:
        print("❌ Error scraping product:", e)
        continue

# Save JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_products, f, ensure_ascii=False, indent=4)

print(f"\n✅ Done! {len(all_products)} products saved to {OUTPUT_FILE}")




# =============================================
# single page multiple product images extract
# =============================================

# import requests
# from bs4 import BeautifulSoup
# import json
# import time

# # --------------- CONFIG ----------------
# CATEGORY_URL = "https://chocolateshopbd.com/product-category/chocolate/feastables/"
# HEADERS = {"User-Agent": "Mozilla/5.0"}
# OUTPUT_FILE = "products.json"
# DELAY_BETWEEN_REQUESTS = 1
# # ---------------------------------------

# all_products = []

# res = requests.get(CATEGORY_URL, headers=HEADERS)
# soup = BeautifulSoup(res.text, "html.parser")

# product_cards = soup.select("a.woocommerce-LoopProduct-link")

# print(f"Found {len(product_cards)} products on this page.")

# for idx, card in enumerate(product_cards, start=1):
#     product_url = card["href"]
#     print(f"{idx}. Scraping product: {product_url}")

#     try:
#         r = requests.get(product_url, headers=HEADERS)
#         s = BeautifulSoup(r.text, "html.parser")

#         # ---- Extract title, description ----
#         title_tag = s.find("h1", class_="product_title")
#         desc_tag = s.find("div", class_="woocommerce-Tabs-panel--description")

#         title = title_tag.text.strip() if title_tag else ""
#         description = desc_tag.text.strip() if desc_tag else ""

#         # ---- Extract images ----
#         image_urls = []

#         # Main image
#         main_img_tag = s.find("img", class_="wp-post-image")
#         if main_img_tag:
#             image_urls.append(main_img_tag.get("src"))

#         # Gallery images
#         gallery_tags = s.select("figure.woocommerce-product-gallery__wrapper img")
#         for img in gallery_tags:
#             src = img.get("src")
#             if src and src not in image_urls:
#                 image_urls.append(src)

#         # ---- Extract prices ----
#         del_tag = s.find("del")   # original price
#         ins_tag = s.find("ins")   # current price

#         def extract_price(tag):
#             if tag:
#                 bdi = tag.find("bdi")
#                 if bdi:
#                     price_text = bdi.get_text().replace("৳","").replace(",","").strip()
#                     try:
#                         return int(float(price_text))
#                     except:
#                         return 0
#             return 0

#         original_price = extract_price(del_tag)
#         current_price = extract_price(ins_tag)
#         if original_price == 0:
#             original_price = current_price

#         # ---- Prepare product dict ----
#         product_data = {
#             "title": title,
#             "current_price": current_price,
#             "original_price": original_price,
#             "description": description,
#             "images": image_urls,
#             "source_url": product_url
#         }

#         all_products.append(product_data)
#         time.sleep(DELAY_BETWEEN_REQUESTS)

#     except Exception as e:
#         print("❌ Error scraping product:", e)
#         continue

# # Save JSON
# with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
#     json.dump(all_products, f, ensure_ascii=False, indent=4)

# print(f"\n✅ Done! {len(all_products)} products saved to {OUTPUT_FILE}")


# =============================================
# send all products data to rest api
# =============================================




