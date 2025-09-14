#парсим все страницы
import requests #импорт бибилиотеки для инета
from bs4 import BeautifulSoup # импортировали библиотеку для парсинга
import time # время
import xlsxwriter # библиотека эксель

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
        #Парсим 1 страницу
        #url = None
    else:
        url = None #закрываем страницу

print("------------------------------")
print(f"Парсинг завершен, найдено {len(data)} цитат")

workbook = xlsxwriter.Workbook("quotes.xlsx") # это создаем эксель файл
worksheet = workbook.add_worksheet("Quotes")# cоздание вкладок в эксель

# вариант №1 - простой
# шаблон форматирования
header_format = workbook.add_format(
    {
        "bold": True,
        "border": 1,
        "align": "center",
        "valign": "vcenter"
    }
)

text_format = workbook.add_format(
    {
        "border": 1,
        "align":  "left",
        "text_wrap": True
}
)


worksheet.set_column(0, 0, 20) # устанавливаем ширину в exel
worksheet.set_column(1, 1, 300) 
worksheet.set_row(0, 30)  #устанавливаем высоту строк

worksheet.write(0, 0, "Author", header_format)
worksheet.write(0, 1, "Quote", header_format)

for row, elem in enumerate(data, start=1):
    worksheet.write(row, 0, elem["author"],text_format)
    worksheet.write(row, 1, elem["quote"],text_format)

workbook.close() # закрыть

print("Файл exel усешно создан")