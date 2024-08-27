import requests
from bs4 import BeautifulSoup


def scrape_news(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return []

    # Parse the content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')

    # Find all the headlines
    headlines = soup.find_all('h3')  # Change the tag as per the website structure

    # Extract and print headline text
    news_headlines = []
    for headline in headlines:
        title = headline.get_text().strip()
        news_headlines.append(title)

    return news_headlines


# URL of the news website you want to scrape
news_url = 'https://www.prothomalo.com/'

# Get the news headlines
headlines = scrape_news(news_url)

# Print the headlines
print("Latest Headlines:")
for index, headline in enumerate(headlines):
    print(f"{index + 1}. {headline}")
