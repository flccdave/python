import requests
from bs4 import BeautifulSoup

# url = "https://phishingdemo.org/python/scraping/4070ti.html"
page = requests.get("https://phishingdemo.org/python/scraping/4070ti.html", headers={"User-Agent": ""})
# print(page.text)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

quantity_of_item = soup.find(id="remaining")
print(quantity_of_item.string)
