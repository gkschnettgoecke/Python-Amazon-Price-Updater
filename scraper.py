import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/dp/B01CKE7B1E/?coliid=I9LSAGND97WT8&colid=1YL9H50D83OM1&psc=1&ref_=lv_ov_lig_dp_it'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


def check_price(new_price):
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id= "productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:4])

    if(converted_price < new_price):
        send_mail()
        return True
    return False
    #print("Price:", converted_price)
    #print("Title:", title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('grant.schnettgoecke@gmail.com', 'nvrrtwnrkexpovzg')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/dp/B01CKE7B1E/?coliid=I9LSAGND97WT8&colid=1YL9H50D83OM1&psc=1&ref_=lv_ov_lig_dp_it'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'grant.schnettgoecke@gmail.com',
        'grant.schnettgoecke@gmail.com',
        msg
    )
    print("Email has been sent!")

    server.quit()

# for i in range(10):
#     check_price()

#End after check price is true
# while(True):
#     if check_price(120):
#         break
#     time.sleep(5)
#     print("Checked Price")

# print("End script")

while(True):
    check_price(120)
    time.sleep(5)