import requests
from bs4 import BeautifulSoup


def get_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('span',{'itemprop': 'price'})['content']
    return price

get
# URL of the website to scrape
url = 'https://wethenew.com/products/'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object with the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Print the links
for link in links:
    print(link.get('href'))
