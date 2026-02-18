import requests
import json

# Load scraped JSON
with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

API_URL = "http://127.0.0.1:8000/api/bulk/import-products"  # your Laravel endpoint
# API_URL = "https://greenworldint.com/bulk/import-products"  # your Laravel endpoint

data = {"products": products}

try:
    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        print("✅ API Response:", response.json())
    else:
        print("❌ Failed:", response.status_code, response.text)
except Exception as e:
    print("❌ Error sending data:", e)
