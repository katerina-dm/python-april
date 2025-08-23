import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\23.08\school.db") # подключили
cursor = connection.cursor() # создали активное подключение
print("База данных усмешно подключена!")

cursor.execute("SELECT  * FROM books") # выполнить запрос
rows = cursor.fetchall() # получить все
#преобразуем в словари
columns = [desc[0] for desc in cursor.description]

data = [dict(zip(columns, row)) for row in rows]

for d in data:
    print(d)

cursor.close() # закрыть доступ