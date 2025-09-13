import requests #импорт бибилиотеки для инета

from bs4 import BeautifulSoup # импортировали библиотеку для парсинга

url = "https://quotes.toscrape.com/"
respons = requests.get(url)


data = []
#парсинг
soup = BeautifulSoup(respons.text, "lxml") 

#ищем все цитаты т.е что попадает под наш фильтр
quotes = soup.find_all("div", class_ = "quote")
# print(len(quotes))

for quote in quotes:
    quote_text = quote.find("span", class_ = "text").get_text(strip=True)
    quote_author = quote.find("small", class_ = "author").get_text(strip=True)

    #print(quote_author.ljust(20, " "), quote_text) 
    d = {"author": quote_author, "quote": quote_text}
    data.append(d)

for elem in data:
    print(elem)
