# Web-Scrapping_Iphone_price-amazon
# Web Scraping for Amazon Products

## Overview
This Python script is designed to scrape product information from Amazon. It extracts data such as product names and prices, and organizes the information into a CSV file.

## Requirements
- Python 3
- Beautiful Soup (`bs4`)
- Requests (`requests`)
- Fake User-Agent (`fake_useragent`)
- Pandas (`pandas`)

## How to Use
1. Clone the repository: `git clone <repository-url>`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the script: `python web_scraping.py`
4. The script will fetch product details from Amazon and create a CSV file named `data.csv` with two columns: `title` and `price`.

## Script Details
- The script uses the Beautiful Soup library to parse HTML content.
- Fake User-Agent is employed to mimic real browser requests.
- Product names are extracted from the HTML tags `<span class="a-size-medium a-color-base a-text-normal">`.
- Prices are extracted from the HTML tags `<span class="a-price">`.
- The extracted data is stored in a dictionary, which is then converted into a Pandas DataFrame and saved as a CSV file.
