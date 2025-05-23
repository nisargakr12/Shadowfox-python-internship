import requests
from bs4 import BeautifulSoup
import csv
import re

# Conversion rate from GBP to INR
GBP_TO_INR = 105

all_books = []

for page in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve page {page}")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        try:
            title = book.h3.a['title']

            # Clean and convert price to INR
            price_text = book.find('p', class_='price_color').text.strip()
            cleaned_price = re.sub(r'[^\d.]', '', price_text)  # Remove £ and any extra characters
            price_gbp = float(cleaned_price)
            price_inr = round(price_gbp * GBP_TO_INR, 2)
            price_display = f"₹{price_inr}"

            # Extract rating
            rating_tag = book.find('p', class_='star-rating')
            rating = rating_tag['class'][1] if rating_tag and len(rating_tag['class']) > 1 else "Not rated"

            all_books.append({
                'title': title,
                'price': price_display,
                'rating': rating
            })

        except Exception as e:
            print(f"Error processing a book on page {page}: {e}")

    print(f"✅ Page {page} scraped.")

# Save to CSV
with open("books_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "price", "rating"])
    writer.writeheader()
    writer.writerows(all_books)

print(f"\n✅ Total books scraped: {len(all_books)}")
print("✅ Data has been saved to books_data.csv")
