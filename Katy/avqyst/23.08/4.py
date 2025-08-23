import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\23.08\school.db") # подключили
cursor = connection.cursor() # создали активное подключение
print("База данных усмешно подключена!")

#создание таблицы

cursor.execute('''
CREATE TABLE IF NOT EXISTS workers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (50) NOT NULL,
    age INTEGER,
    profession VARCHAR (50) NOT NULL
)
''')

connection.commit() # применить изменения