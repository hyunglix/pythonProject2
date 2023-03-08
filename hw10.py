from bs4 import BeautifulSoup
import requests
import sqlite3

response = requests.get("https://weather.com/weather/today/l/28d4e480b2d9d9940abbb37a6287f2017855022d9a334e86f36addde0b0179da")
connection = sqlite3.connect("C:\itstep2.sl3", 5)
cur = connection.cursor()
# cur.execute("CREATE TABLE temperature_table (temperature TEXT);")
