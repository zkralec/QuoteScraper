import requests
import csv

from bs4 import BeautifulSoup
from urllib.parse import urljoin

# GET request
url = 'https://quotes.toscrape.com'
response = requests.get(url)

# Parsing the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Get the block with the quote
quote_block = soup.find_all('div', 'quote')

# Writing quotes and authors to a CSV
quote_file = open('quotes.csv', mode='w', newline='', encoding='utf-8')
writer = csv.writer(quote_file)
writer.writerow(['Quote', 'Author'])

# Getting next page block
next_block = soup.find_all('li', 'next')

# Finding the correct tag and getting the joinable href
for i in next_block:
    temp = i.find('a')
    href = temp.get('href')

while href is not None:
    
    # Request new url
    response = requests.get(urljoin(url, href))

    # Parsing ne HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the block with the quote
    quote_block = soup.find_all('div', 'quote')

    # Looping through the block and extracting the quote and author block
    for i in quote_block:
        quote = i.find('span', 'text').get_text()
        author = i.find('small', 'author').get_text()
        writer.writerow([quote, author])

    # Getting next block and hyperlink reference
    next_block = soup.find('li', 'next')

    # Set the hyperlink reference if there is a next button, else stop
    href = next_block.find('a')['href'] if next_block else None

# Closing the CSV file
quote_file.close()
print("DONE: Check the 'quotes.csv' file for all scraped quotes")
