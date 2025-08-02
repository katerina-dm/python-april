import json

json_data = '{"name": "Sharik", "age": 3, "color": "gren"}'

#конвертируем в обьект, загружает json из строки и конвертирует его в язык пайтон
data = json.loads(json_data)

print(data["name"])
print(type(data))