# методы множества

a = {12,24,45,457,67,976,708,568,754,32,434}
print(a)

a.add(22) # довавляем . только уникальные элементы
print(a)

a.remove(24)# удаляем те элементы которые есть
print(a)

a.discard(0)# удаляем даже если нет, то ошибки не будет,все останется как есть
print(a)

number = a.pop() # удаляет случайный элемент
print(number)
print(a)

a.clear()# полностью очищает
print(a)
