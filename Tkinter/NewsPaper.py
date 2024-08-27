import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, ttk
import webbrowser

def scrape_news(url):
    """Scrape news headlines and their URLs from the specified URL."""
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            messagebox.showerror("Error", f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return []

        # Parse the content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'lxml')

        # Find all the headlines and their links
        headlines = soup.find_all('h3')
        news_headlines = []
        for headline in headlines:
            # Get the headline text
            title = headline.get_text().strip()
            # Find the link within the headline tag (this may vary depending on the website's HTML structure)
            link_tag = headline.find('a')
            if link_tag is not None:
                link = link_tag['href']
                # Append the base URL if the link is relative
                if not link.startswith('http'):
                    link = url + link
                news_headlines.append((title, link))

        return news_headlines
    except requests.RequestException as e:
        messagebox.showerror("Error", f"An error occurred while fetching the news: {e}")
        return []

def display_headlines():
    """Fetch and display news headlines with links in the Tkinter GUI."""
    # Get the URL from the user input
    news_url = url_entry.get().strip()

    # Validate the URL
    if not news_url:
        messagebox.showwarning("Input Error", "Please enter a valid URL.")
        return

    # Ensure the URL starts with 'https://'
    if not news_url.startswith("http://") and not news_url.startswith("https://"):
        news_url = "https://" + news_url

    headlines = scrape_news(news_url)
    if headlines:
        # Clear previous headlines
        headlines_textbox.delete('1.0', tk.END)

        # Display the headlines in the GUI
        for idx, (headline, link) in enumerate(headlines, start=1):
            # Insert the headline and add a tag to make it clickable
            start_index = headlines_textbox.index(tk.END)
            headlines_textbox.insert(tk.END, f"{idx}. {headline}\n", f"headline_{idx}")
            headlines_textbox.tag_bind(f"headline_{idx}", "<Button-1>", lambda e, url=link: open_link(url))

            # Insert a new line for spacing
            headlines_textbox.insert(tk.END, "\n")

        # Enable all hyperlinks
        headlines_textbox.config(state=tk.NORMAL)
    else:
        messagebox.showinfo("Information", "No headlines found. Please check your internet connection and try again.")

def open_link(url):
    """Open the specified URL in a web browser."""
    webbrowser.open_new(url)

# Create the main Tkinter window
root = tk.Tk()
root.title("Latest News Headlines")
root.geometry("600x450")

# Create a frame for URL input
url_frame = ttk.Frame(root)
url_frame.pack(fill='x', padx=10, pady=5)

# URL entry label and widget
url_label = ttk.Label(url_frame, text="Enter News Website URL:")
url_label.pack(side='left', padx=(0, 10))
url_entry = ttk.Entry(url_frame, width=50)
url_entry.pack(side='left', fill='x', expand=True)

# Create a frame to hold the headlines text box
headlines_frame = ttk.Frame(root)
headlines_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Create a text widget with a vertical scrollbar
headlines_textbox = tk.Text(headlines_frame, wrap='word', height=15)
headlines_textbox.pack(side='left', fill='both', expand=True)

# Add a scrollbar to the text widget
scrollbar = ttk.Scrollbar(headlines_frame, orient='vertical', command=headlines_textbox.yview)
scrollbar.pack(side='right', fill='y')
headlines_textbox.config(yscrollcommand=scrollbar.set)

# Add a button to fetch and display headlines
fetch_button = ttk.Button(root, text="Fetch Latest Headlines", command=display_headlines)
fetch_button.pack(pady=10)

# Run the main event loop
root.mainloop()
