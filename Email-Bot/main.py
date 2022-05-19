import datetime as dt
import smtplib
import random
# declarations
my_email = "testemail@gmail.com"
password = "88888888"
now = dt.datetime.now()
day_of_week = now.weekday()
quotes = []
# getting quotes from file and removing \n from them.
with open("quotes.txt") as file:
    quotes_unedited = (file.readlines())
    for quote in quotes_unedited:
        quotes.append(quote.strip())
# connecting to the SMTP of gmail.com, loging into account and sending email.
with smtplib.SMTP("smtp.gmail.com") as connection:
    generate_email = quotes[random.randint(0, len(quotes) - 1)]
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="fady.shenouda613@gmail.com",
                        msg="Subject: This email is programed by Fady Shenouda\n\n This is the body of my email!")

