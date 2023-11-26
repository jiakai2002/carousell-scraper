import csv

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
URL = "https://carousell.sg/search/macbook/"
driver.get(URL)

HEADERS = {
    "User Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Accept-Language": "en-US, en;q=0.5",
}

soup = BeautifulSoup(driver.page_source, "html.parser")


def select_item(tag):
    return tag.has_attr("data-testid") and "listing-card" in tag.get("data-testid")


def select_link(tag):
    return tag.has_attr("href") and "referrer_browse_type" in tag.get("href")


i = 0
items = soup.find_all(select_item)
data = []
for item in items:
    tags = item.find_all("p")
    item_data = []
    # add data to item_data
    for tag in tags:
        s = tag.text
        if s and s != "Free delivery" and s != "Buyer Protection":
            item_data.append(s)
    tagL = item.find(select_link)
    # add link to item_data
    if tagL:
        link = "https://carousell.sg" + tagL.get("href")
        item_data.append(link)
    if item_data:
        data.append(item_data)
print(data)


header = ["Name", "Date", "Title", "Price", "Condition", "Link"]

with open("data.csv", "w", newline="", encoding="UTF8" as f)
    writer = csv.writer(f)
    writer.writerow(header)
    for d in data:
        writer.writerow(d)



