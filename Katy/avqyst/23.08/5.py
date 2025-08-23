import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\23.08\school.db") # подключили
cursor = connection.cursor() # создали активное подключение
print("База данных усмешно подключена!")

cursor.execute("SELECT * FROM workers") # выполнить запрос
rows = cursor.fetchall() # получить все

columns = [desc[0] for desc in cursor.description]
print(columns)

cursor.close() # закрыть доступ