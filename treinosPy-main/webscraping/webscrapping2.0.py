from bs4 import BeautifulSoup
import requests

URL = "https://a.co/d/cmXPou4"

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

site = requests.get(URL, headers = headers)
soup = BeautifulSoup(site.content, 'html.parser')

#title = soup.find('h1 id', class_ = 'a-size-large a-spacing-none')
price = soup.find('span', class_ = 'a-price-whole').get_text()


num_price = price[3:].replace(",", "")
'''
num_price = num_price[0:len(num_price)-2]
num_price = float(num_price)

if(num_price < 75):
    print("opa")
else:
    print("ah?")
'''

print(num_price)