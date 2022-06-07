import os  # import to get enviroment variables
import requests  # import to get html text.
from bs4 import BeautifulSoup  # import to parse and select through html text.
import smtplib  # import to start SMTP connection and send email.

headers = {  # Headers required from amazon website
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}
BUY_PRICE = 25 # Buy Price of book. 
URL = "https://www.amazon.ca/Subtle-Art-Not-Giving-Counterintuitive/dp/0062457713/ref=tmm_hrd_swatch_0?_encoding=UTF8&qid=&sr=" #AMAZON URL LINK
response = requests.get(url=URL, headers=headers) #Getting Html link
html = BeautifulSoup(response.text, "html.parser") # Parsing html
title = html.select_one(id="productTitle") # getting the product title.
item_price = float(html.select_one("span .a-offscreen").getText().strip("$")) # getting item price.
if item_price < BUY_PRICE: # Sending email in the case of item price drops under the price we are looking for.
    message = f"{title} is now {item_price} link:{URL}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL"], os.environ["Password"])
        connection.sendmail(
            from_addr=os.environ["EMAIL"],
            to_addrs=os.environ["EMAIL"],
            msg=f"Subject: Amazon Price Alert! \n\n {message} \n"
        )
