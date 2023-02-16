import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

TARGET_PRICE = 250
MY_EMAIL = "omrirahmaniking@gmail.com"
MY_PASSWORD = "vdagsksjfkqxtpcy"

product_url = "https://www.amazon.com/Ninja-IG651-Griddle-Dehydrate-Thermometer/dp/B09B82LJ21/ref=sr_1_1_sspa?keywords=ninja%2Bgrill%2Bag651&qid=1676539969&sprefix=ninja%2Bgrill%2Bag%2Caps%2C216&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNUVVQjE5NVpVWE1XJmVuY3J5cHRlZElkPUEwNTgyMzg3MUk0QzZTNzZaWkdKSyZlbmNyeXB0ZWRBZElkPUEwNjY1NDg0M0xLNVE3VDgwU1EzQiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1"
response = requests.get(product_url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Language":"en-US"})

soup = BeautifulSoup(response.text, "lxml")

price = soup.find(class_="a-offscreen")
price_as_float = float(price.text.replace("$", ""))
print(price_as_float)

if(price_as_float <= TARGET_PRICE):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:New Low Price of ninja ig651!\n\nNew Low Price of ninja ig651! \n\nJUST:{price.text}!!!\n\n link ={product_url}".encode('utf-8')
            )
else:
    print(False)