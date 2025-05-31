fruit = ("apple", "banana", "orang", "lemon","apple","apple","lemon")

user_choice = input("Введите название фрукта: ") #справшиваем у пользователя
count = fruit.count(user_choice)

if count:
    print(f"{user_choice} встречается в кортеже {count} раз")
else:
    print("такого нет у нас")