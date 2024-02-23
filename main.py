import csv
import subprocess
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

product = input("Enter Product: ").replace(" ", "%20") + "/?"
price = "&price_start=" + input("Enter Min Price: ")
count = int(int(input("Enter number of listings: ")) / 40)
driver = webdriver.Chrome()
URL = "https://id.carousell.com/search/" + product + price
driver.get(URL)

xp = '//*[@id="main"]/div[2]/div/section[3]/div[1]/div/button'


def check_exists_by_xpath(xp):
    try:
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, xp)
    except NoSuchElementException:
        return False
    return True


for i in range(0, count):
    if check_exists_by_xpath(xp):
        driver.find_element(By.XPATH, xp).click()
    else:
        break

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
        link = "https://id.carousell.com" + tagL.get("href")
        item_data.append(link)
    if item_data:
        data.append(item_data)
        i += 1
header = ["Name", "Date", "Title", "Price", "Condition", "Link"]

# Format tanggal dan waktu saat ini
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

# Nama file CSV sesuai dengan tanggal dan waktu saat ini
csv_file_name = f"data_{current_datetime}.csv"

# Menulis file CSV dengan delimiter titik koma
with open(csv_file_name, "w", newline="", encoding="UTF8") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(header)
    for d in data:
        writer.writerow(d)
driver.quit()

print("Completed!", i, "new listings added to", csv_file_name)
if input("Open CSV file?(y/n): ") == "y":
    subprocess.call(["start", "excel", csv_file_name], shell=True)
