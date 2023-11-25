from bs4 import BeautifulSoup
from selenium import webdriver

item = input("Enter item you are searching for: ")
item = item.replace(" ", "%20") + "/?"
price = (
    "&price_start="
    + input("Enter min price: ")
    + "&price_end="
    + input("Enter max price: ")
)
inp = input(
    "Enter condition:(1=brandnew, 2=likenew, 3=lightlyused, 4=wellused, 5=heavilyused): "
)
if inp == "1":
    condition = "layered_condition=3&"
elif inp == "2":
    condition = "layered_condition=3%2C4&"
elif inp == "3":
    condition = "layered_condition=3%2C4%2C7&"
elif inp == "4":
    condition = "layered_condition=3%2C4%2C7%2C5&"
else:
    condition = "layered_condition=3%2C4%2C7%2C5%2C6&"

inp = input("Choose sort by(1=best match, 2 = price, 3 = recent): ")
if inp == "1":
    sortby = "&sort_by=1"
elif inp == "3":
    sortby = "&sort_by=3"
else:
    sortby = "&sort_by=4"

driver = webdriver.Chrome()
URL = "https://carousell.sg/search/" + item + condition + price + sortby
driver.get(URL)

HEADERS = {
    "User Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Accept-Language": "en-US, en;q=0.5",
}

soup = BeautifulSoup(driver.page_source, "html.parser")


def selector(tag):
    return tag.has_attr("href") and "browse_type" in tag.get("href")


i = 0
links = soup.find_all(selector)
for link in links:
    tags = link.find_all()
    if len(tags) == 8:
        i += 1
        print(i, ")", tags[3].string)
        print(tags[5].string)
        print(tags[6].string)
    elif len(tags) == 10:
        i += 1
        print(i, ")", tags[5].string)
        print(tags[7].string)
        print(tags[8].string)
