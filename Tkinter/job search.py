from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options (headless mode to run without opening a browser window)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Provide path to the ChromeDriver executable
chrome_service = Service('/path/to/chromedriver')  # Update with the path to your ChromeDriver

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the Jobly job listings page
url = "https://www.jobly.fi/en/jobs"
driver.get(url)

# Wait for the page to load completely
driver.implicitly_wait(10)  # You can adjust the wait time if needed

# Find all job listings (adjust the selector based on the site's structure)
job_listings = driver.find_elements(By.CLASS_NAME, "job-item")  # Example class, adjust as needed

# Check if any jobs were found
if job_listings:
    for job in job_listings:
        # Extract the job title
        job_title = job.find_element(By.CLASS_NAME, "job-title").text

        # Extract the job link
        job_link = job.find_element(By.TAG_NAME, "a").get_attribute("href")

        # Extract the company name
        company = job.find_element(By.CLASS_NAME, "company-name").text

        # Extract the job location
        location = job.find_element(By.CLASS_NAME, "location").text

        # Print the job details
        print(f"Job Title: {job_title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print(f"Job Link: {job_link}")
        print("-" * 40)
else:
    print("No job listings found.")

# Close the browser
driver.quit()
