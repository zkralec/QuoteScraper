import requests
from bs4 import BeautifulSoup

# GET request
url = "https://quotes.toscrape.com"
response = requests.get(url)

# Parsing the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Get the block with the quote
quote_block = soup.find_all("div", "quote")

# Looping through the block and extracting the quote and author block
for i in quote_block:
    quote = i.find("span", "text").get_text()
    author = i.find("small", "author").get_text()
    print(quote + " - " + author)
