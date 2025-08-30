import requests # библиотека для HTPP запросов


url = "https://www.google.com"

response = requests.get(url) # выполнить запрос с помощью метода cet

print(f"Код ответа: {response.status_code}") # посмотреть какой метод

#print(f"Заголовок: ")
#for key, value in response.headers.items():
#print(f"{key}: {value}")

print(f"Тело страницы: {response.text}")

with open("google.html", "w", encoding="utf-8") as fl:
    fl.write(response.text)