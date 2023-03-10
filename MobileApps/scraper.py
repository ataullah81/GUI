import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/' \
      'Camcorder-ORDRO-Microphone-Handheld-Storage/dp/B083JZT5CF/ref=sr_1_1_sspa?crid=S3DQYKK3QM3N&keywords=prime+video+camera&qid=1677937586&sprefix=prime+video+camara%2Caps%2C212&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRFA4SkVCSDQ2WjRPJmVuY3J5cHRlZElkPUEwNjg2MTUwQzNIOUdQMjdGUEo0JmVuY3J5cHRlZEFkSWQ9QTAzNTU2NTYyTUxOUkxFT0hFTldaJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id = 'productTitle').get_text()
price = soup.find(id = "priceblock_ourprice").get_text()
print(title.strip())