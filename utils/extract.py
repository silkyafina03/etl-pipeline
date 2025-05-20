# utils/extract.py
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

def extract_product_data(card):
    title = card.select_one(".product-title").text.strip()
    price = card.select_one(".price").text.strip()

    info_paragraphs = card.select(".product-details p")
    rating, colors, size, gender = "", "", "", ""

    for p in info_paragraphs:
        text = p.text.strip()
        if "Rating:" in text:
            rating = text.replace("Rating: ⭐", "").replace("/ 5", "").strip()
        elif "Colors" in text:
            colors = text.split(" ")[0]
        elif "Size:" in text:
            size = text.replace("Size:", "").strip()
        elif "Gender:" in text:
            gender = text.replace("Gender:", "").strip()

    return {
        "title": title,
        "price": price,
        "rating": rating,
        "colors": colors,
        "size": size,
        "gender": gender
    }

def fetch_page_content(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil {url}: {e}")
        return None



def get_next_page_url(soup, current_url):
    next_button = soup.select_one(".pagination .next a")
    if next_button and 'href' in next_button.attrs:
        relative_url = next_button.attrs['href']
        return urljoin(current_url, relative_url)
    return None


def extract_data_from_url(start_url):
    all_product_data = []
    current_url = start_url

    while current_url:
        print(f"Scraping: {current_url}")
        content = fetch_page_content(current_url)
        if not content:
            break

        soup = BeautifulSoup(content, 'html.parser')
        cards = soup.select(".collection-card")

        data = [extract_product_data(card) for card in cards]
        all_product_data.extend(data)

        current_url = get_next_page_url(soup, current_url)

    return pd.DataFrame(all_product_data)
