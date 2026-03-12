import csv
from datetime import datetime
import time
from scraper import get_price
from products import products
from telegram_bot import send_message

alerted_products = set()
while True:

    for product in products:

        price = get_price(product["url"])

        if price:

            print(product["name"], price)

            with open("prices.csv", "a", newline="") as file:

                writer = csv.writer(file)
                writer.writerow([
                datetime.now(),
                product["name"],
                price
    ])

            if price <= product["target_price"] and product["name"] not in alerted_products:
                msg = f'Price droped!\n{product["name"]}\nPrice: {price}\n{product["url"]}'
                print(msg)
                send_message(msg)
                alerted_products.add(product["name"])
    time.sleep(2)

    print("verifing again...")
    time.sleep(600)