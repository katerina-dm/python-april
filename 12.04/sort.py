#lst = [456,34, 35, 1, 235, 346, 33,78]

#lst.sort() # сортируем от меньшего к большему
#print(lst)

#lst.sort(reverse=True) # сортируем от большего к меньшему
#print(lst)

employers = [
    ["Иван", "Иванов", 1000 , 20],
    ["Сергей", "Сергеев", 800, 35],
    ["Светлана", "Иванова", 1500, 15],
    ["Анатолий", "Червяк", 2000, 1],
    ["Арнольд", "Шварцнегер", 3000, 0], 
    ["Сильвестр", "Сталоне", 300 , 60]  
    ]

for i in employers:
    print(i)

employers.sort()# отсортировано по имени
print("=" *35)
for i in employers:
    print(i)


employers.sort(key=lambda x: x[2]) #ключ..2 это индекс...отсортировали по ставке
print("=" *35)
for i in employers:
    print(i)

employers.sort(key=lambda x: x[2], reverse=True) #отсортировали от меньшего к большему
print("=" *35)
for i in employers:
    print(i)

employers.sort(key=lambda x: x[2]*x[3], reverse=True) #умножили ставку на смену, мак зп
print("=" *35)
for i in employers:
    print(i)