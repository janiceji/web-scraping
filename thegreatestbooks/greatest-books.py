import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
URL = 'https://thegreatestbooks.org/?page='
# for page in range(1,55)
# page = 1

books = []
authors = []
for page in range(1,55):
    req = requests.get(URL + str(page))
    soup = bs(req.text, 'html.parser')
    container = soup.findAll("div", {"class":"container"})
#     first_book = container[3]
#     first_book.h4.a.text
#     first_book.h4.findAll("a")[1].text

    for book in container:
        try:
            if book.h4.findAll("a")[0].text != "" and book.h4.findAll("a")[1].text != "":
                books.append(book.h4.findAll("a")[0].text)
                authors.append(book.h4.findAll("a")[1].text)
            else:
                books.append("na")
                authors.append("na")
        except:
            books.append("na")
            authors.append("na")

df = pd.DataFrame(books,authors)
df.to_csv('greatest.csv')
