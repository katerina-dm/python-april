#setdefault - установить по умолчанию

worker = {
    "name": "Иван",
    "fname": "Иванов",
    "profession": "Баскетболист",
    "salary": 500_000
}

worker.setdefault("age", 0)
worker.setdefault("age", 30)
print(worker)

# метод pop - удаление
name = worker.pop("name")
print(f"Удалили из словаря {name}")
print(worker)

# метод popitem - удаление из словаря последний добавленный элемент
name = worker.popitem()
print(f"Удалили из словаря {name}")
print(worker)

# метод clear -очищает полностью словарь
#name = worker.clear()
#print(worker)

# метод copy - копировать
#worker1 = worker

#worker1.clear()
#print(worker)
#print(worker1)

worker1 = worker.copy()
worker1['age'] = 100
print(worker)
print(worker1)
