lst = [10, 12, 13, "apple", 15, True,34] #изменить список
print(lst)

lst [3] = 14
print(lst)

lst.insert(1,11) #вставили между 10 и 12 - 11...1 -это элемент списка
print(lst)

lst.extend([16,17])# добавить несколько элементов в конец списка
print(lst)

lst.remove(True) #удаляет первое вхождение этого слова
print(lst)

lst.pop(6) #удаляет по индексу элемент
print(lst)