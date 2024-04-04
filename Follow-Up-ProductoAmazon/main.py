""" program that notifies you when your favorite product drops in price """ 
""" Complete your : smtp, email, passwor"""
import requests  
import lxml
from bs4 import BeautifulSoup  
import smtplib  

BUY_MY_DEAR = 200

URL = "https://www.amazon.com/-/es/Computadora-port%C3%A1til-almacenamiento-microborde-Microsoft/dp/B0947BJ67M/ref=sr_1_3?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-3" 
PARAMS = { 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.5"
} 

response = requests.get(URL, headers=PARAMS) 
soup = BeautifulSoup(response.content, "lxml") 
print(soup.prettify()) 

price = soup.find(class_="a-offscreen").getText() 
money = prince.split("$")[1] 
money_float = float(money) 
print(money_float) 

title = soup.find(id="productoTitle").getText().strip()  
 
if money_float < BUY_MY_DEAR: 
    ms = f"{title} is now {price}" 

    with smtplib.SMTP("YOUR_SMTP_ADDRES", port=587) as connection: 
        connection.starttls("jcrecalde30@gmail.com", "PASSWORD") 
        Connection.sendmail( 
            from_addr="jcrecalde30@gmail.com",
            to_addrs="jcrecalde30@gmail.com", 
            msg=f"Subject: Amazon Price Alert !!!\n\n{ms}\n{URL}".encode("utf-8")
        )

