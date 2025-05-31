lst = [10, 12, 13, "apple", 15, True,34]
for elem in lst: #вывели списки
    print(elem)

print(lst)

#for i in range(len(lst)): #вывели индексы, len определяем длину списка
    #print(i)

for i in range(len(lst)): #i = от 0 до 6
    lst[i] = i + 10

print(lst)