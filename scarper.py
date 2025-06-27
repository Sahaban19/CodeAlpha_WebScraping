import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL to scrape
URL = "https://timesofindia.indiatimes.com/city/kolkata"

# Send GET request
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
data = []

# Extract headlines from <h3> tags
headlines = soup.find_all("h2")
for tag in headlines:
    headline = tag.get_text(strip=True)
    
    # Try to get the link (if inside <a> tag)
    link_tag = tag.find("a")
    link = link_tag['href'] if link_tag and link_tag.has_attr('href') else ""

    data.append({
        "Headline": headline,
        "Link": link
    })

# Create folder if it doesn’t exist
os.makedirs("data", exist_ok=True)

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("data/headlines.csv", index=False)

print("✅ Headlines saved to data/headlines.csv")
