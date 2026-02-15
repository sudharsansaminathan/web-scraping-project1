import requests
from bs4 import BeautifulSoup
import pandas as pd

quotes = []
authors = []
tags = []

page = 1

while len(quotes) < 15:
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quote_blocks = soup.find_all("div", class_="quote")

    for block in quote_blocks:
        if len(quotes) >= 15:
            break
        
        quote = block.find("span", class_="text").text
        author = block.find("small", class_="author").text
        
        tag_list = block.find_all("a", class_="tag")
        tag_text = ", ".join([tag.text for tag in tag_list])

        quotes.append(quote)
        authors.append(author)
        tags.append(tag_text)

    page += 1

data = pd.DataFrame({
    "Quote": quotes,
    "Author": authors,
    "Tags": tags
})

data.to_excel("Quotes_file.xlsx", index=False)

print(" file created successfully")
