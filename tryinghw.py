from bs4 import BeautifulSoup
import sqlite3
import datetime
import time
import requests
response = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BC%D0%B5%D1%80%D1%96%D0%BD%D0%B3")


# cur.execute("CREATE TABLE temperature (city TEXT, data TEXT, temperature TEXT);")
while True :
    connection = sqlite3.connect("C:\itstep2.sl3", 5)
    cur = connection.cursor()
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        temp = soup.find("p", {"class" : "today-temp"})
        # res = soup_list[0].find("span")
        print(temp.text)
        temperature = temp.text
        cur.execute(f"INSERT into temperature values ('Mering', '{datetime.datetime.now()}', '{temperature}');")
        connection.commit()
        connection.close()
        time.sleep(1800)
