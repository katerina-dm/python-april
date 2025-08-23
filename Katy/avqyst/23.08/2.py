import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\23.08\school.db") # подключили
cursor = connection.cursor() # создали активное подключение
print("База данных усмешно подключена!")

cursor.execute("SELECT books.title FROM books") # выполнить запрос
rows = cursor.fetchall() # получить все
for row in rows:
    print(row)

cursor.close() # закрыть доступ