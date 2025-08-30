import requests # библиотека для HTPP запросов


url = "https://www.google.com/search"

params = {
    "q": "что покушать на ужин"
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
}

response = requests.get(
    url=url , 
    params = params, 
    headers=headers) # выполнить запрос с помощью метода cet

print(f"Код ответа: {response.status_code}") # посмотреть какой метод


print(f"Тело страницы: {response.text}")

with open("2.html", "w", encoding="utf-8") as fl:
    fl.write(response.text)