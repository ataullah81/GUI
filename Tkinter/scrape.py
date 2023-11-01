import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # You need to have Chrome and chromedriver installed

# Specify the Google Scholar URL and search query
google_scholar_url = "https://scholar.google.com"
search_query = "Python programming"

# Open Google Scholar and perform the search
driver.get(google_scholar_url)

# Locate the search input field by its XPath
search_box = driver.find_element_by_xpath("//input[@name='q']")
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Scroll down the page to load more results (you may need to adjust the number of scrolls)
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Get the page source and parse it with Beautiful Soup
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

# Find and collect the search results
results = soup.find_all("div", {"class": "gs_ri"})

# Create a list to store the data
data = []

# Extract data from each result
for result in results:
    title = result.find("h3", {"class": "gs_rt"}).get_text()
    authors = result.find("div", {"class": "gs_a"}).get_text()
    link = result.find("h3", {"class": "gs_rt"}).find("a")["href"]

    data.append([title, authors, link])

# Close the WebDriver
driver.quit()

# Save the data to a CSV file
csv_filename = "google_scholar_results.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Title", "Authors", "Link"])
    csv_writer.writerows(data)

print(f"Data saved to {csv_filename}")
