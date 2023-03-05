from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.oschadbank.ua/currency-rate")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td", {"class" : "heading-block-currency-rate__table-col"})
    res = soup_list[10]
b = float(res.text)
a = int(input("Введіть суму у грн:"))
c = a/b
print(round(c,1))

