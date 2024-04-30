from bs4 import BeautifulSoup
import requests

URL = "https://www.amazon.com.br/dp/8581052983/?coliid=I1GRKT9FXHD6X2&colid=3PK5X0MC70IVC&psc=1&ref_=lv_ov_lig_dp_it"

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

site = requests.get(URL, headers = headers)

soup = BeautifulSoup(site.content, 'html.parser')

'''title = soup.find('h1', class_ = 'a-spacing-none a-text-normal')'''
price = soup.find('span', class_ = 'a-size-base a-color-price a-color-price').get_text().strip()

num_price = price[3:9].replace(",", "")
num_price = num_price[0:len(num_price)-2]
num_price = float(num_price)

if(num_price < 25):
     print("opa")
else:
     print("ah?")

print(num_price)