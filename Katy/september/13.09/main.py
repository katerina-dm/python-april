import requests #импорт бибилиотеки для инета

from bs4 import BeautifulSoup # импортировали библиотеку для парсинга

url = "https://quotes.toscrape.com/"
respons = requests.get(url)
# print(respons.status_code)
# print(respons.text)

#парсинг
# название переменной любое придумываем
soup = BeautifulSoup(respons.text, "lxml")  #lxml это бибилиотека

#print(soup.text) # очистили от тегов кодов
#print(soup.prettify()) # преобразованная страница html красиво

#парсим цитаты
quote = soup.find("div", class_ = "quote")
#print(quote.text)
#print(quote.prettify())

# ищем первую цитату только текст
quote_text = quote.find("span", class_ = "text").get_text(strip=True)
quote_author = quote.find("small", class_ = "author").get_text(strip=True)
print(quote_text)
print(quote_author)