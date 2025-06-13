import requests
import csv
from bs4 import BeautifulSoup

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

# Creating empty list
list = []

# Looping through the block and extracting the quote and author block
for i in quote_block:
    quote = i.find('span', 'text').get_text()
    author = i.find('small', 'author').get_text()
    list.append([quote, author])

# Looping through list and writing each quote/author
for i in list:
    writer.writerow(i)

# Closing the CSV file
quote_file.close()
