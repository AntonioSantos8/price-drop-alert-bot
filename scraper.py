import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_price(url):

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.find("span", class_="andes-money-amount__fraction")

    if price_element:
        price = price_element.text
        price = price.replace(".", "")
        return float(price)

    return None