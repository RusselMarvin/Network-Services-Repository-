import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = 'https://www.yahoo.com/'

# Send the request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Scraping articles...")

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all h3 tags, we can filter them by relevant classes (like those containing news titles)
    h3_tags = soup.find_all('h3')

    # List to store the article titles
    article_titles = []

    # Loop through the h3 tags and filter relevant articles (you may need to adjust this)
    for h3 in h3_tags:
        # Attempt to get text or the anchor tag inside the h3
        title = h3.get_text(strip=True)
        if title:  # Only add non-empty titles
            article_titles.append(title)

    # If no articles found, print a message
    if article_titles:
        print(f"Found {len(article_titles)} articles:")

        # Open the file in write mode and write the articles
        with open('news.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Number', 'News'])  # Write the header row
            # Write each article
            for idx, title in enumerate(article_titles, start=1):
                scraped_text = [idx, title]  # Create a list with index and title
                writer.writerow(scraped_text)  # Write the row to the CSV file
                print(f"{idx}. {title}")  # Print the article title

    else:
        print("No articles found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
