worker = {
    "name": "Иван",
    "fname": "Иванов",
    "age": 25,
    "profession": "Баскетболист",
    "salary": 500_000
}

worker["start_date"] = "12.12.12" #в фигурных скобках несущетсвующий список, а равно то что добавляем

#print(worker)
print (f"{worker["profession"]} по имени {worker["name"]} в возрасте {worker["age"]} лет, получает {worker["salary"]} $ ")