import json

#словарь
data = {
    "name" : "Sharik",
    "age" : 3,
    "color": "gren"
     }
#переводим в json формат
json_data = json.dumps(data)
print(json_data)