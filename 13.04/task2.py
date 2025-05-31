fruit = ("apple", "banana", "orang", "lemon","apple","apple","lemon","bananamango")

user_choice = input("Введите название фрукта: ") #справшиваем у пользователя
count = len(tuple(filter(lambda x: user_choice in x, fruit)))

if count:
    print(f"{user_choice} встречается в кортеже {count} раз")
else:
    print("такого нет у нас")