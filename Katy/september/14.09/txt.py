#парсим все страницы
import requests #импорт бибилиотеки для инета
from bs4 import BeautifulSoup # импортировали библиотеку для парсинга
import time

data = []

base_url = "https://quotes.toscrape.com"
url = base_url

while url:
    time.sleep(2)
    respons = requests.get(url)
    #парсинг
    soup = BeautifulSoup(respons.text, "lxml")
    #парсим цитаты
    quotes = soup.find_all("div", class_ = "quote")

    for quote in quotes:
        quote_text = quote.find("span", class_ = "text").get_text(strip=True)
        quote_author = quote.find("small", class_ = "author").get_text(strip=True)

        d = {"author": quote_author, "quote": quote_text}
        data.append(d)

    next_btn = soup.find("li", class_ = "next")
    if next_btn:
        url = base_url + next_btn.a["href"]
        print(url)
    else:
        url = None #закрываем страницу

with open("quotes.txt", "w",encoding="utf-8") as fl:
    for elem in data:
        fl.write(
            f"{elem['author'].ljust(20, ' ')}{elem['quote']}\n"
        )


print("------------------------------")
print(f"Парсинг завершен, найдено {len(data)} цитат")
