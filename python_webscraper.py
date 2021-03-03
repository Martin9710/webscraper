import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL= 'https://www.amazon.se/Super-Smash-Ultimate-Nintendo-Switch/dp/B07BC272SC/ref=sr_1_1?dchild=1&keywords=Super+smash+bros&qid=1606440300&sr=8-1'


headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = int(price[0:3])

    print(converted_price)

    if(converted_price < 450):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mail1@gmail.com', 'xxxxx')

    subject = 'Price fell down mathafacka'
    body = 'Check it: https://www.amazon.se/Super-Smash-Ultimate-Nintendo-Switch/dp/B07BC272SC/ref=sr_1_1?dchild=1&keywords=Super+smash+bros&qid=1606440300&sr=8-1'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'mail1@gmail.com',
        'mail2@outlook.com',
        msg
    )

    print('MAIL SENT')

    server.quit()

check_price()
