#парсим одну  страницу
import requests #импорт бибилиотеки для инета

from bs4 import BeautifulSoup # импортировали библиотеку для парсинга

base_url = "https://quotes.toscrape.com"
respons = requests.get(base_url)

#парсинг
soup = BeautifulSoup(respons.text, "lxml")  #lxml это бибилиотека

#парсим цитаты
quotes = soup.find_all("div", class_ = "quote")

data = []

for quote in quotes:
    quote_text = quote.find("span", class_ = "text").get_text(strip=True)
    quote_author = quote.find("small", class_ = "author").get_text(strip=True)

    d = {"author": quote_author, "quote": quote_text}
    data.append(d)

next_btn = soup.find("li", class_ = "next")
if next_btn:
    url = base_url + next_btn.a["href"]
    print(url)


#print(next_btn.prettify())