import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd

ua = UserAgent()
header = {"User-Agent": str(ua.chrome)}

# URL to scrape
url = "https://www.amazon.in/s?k=iphone&crid=3AULCQNDKJVMX&sprefix=iphone%2Caps%2C257&ref=nb_sb_noss_1"
r = requests.get(url, headers=header)
soup = BeautifulSoup(r.text, 'html.parser')

data = {'title': [], 'price': []}

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")

for span, price in zip(spans, prices):
    title = span.string
    price_text = price.find("span").get_text()

    print(title)
    print(price_text)

    data['title'].append(title)
    data['price'].append(price_text)

df = pd.DataFrame.from_dict(data)

df.to_csv("data.csv", index=False)
