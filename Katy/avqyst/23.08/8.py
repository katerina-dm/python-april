import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\23.08\school.db") # подключили
cursor = connection.cursor() # создали активное подключение
print("База данных усмешно подключена!")

new_workers = [("Евлампий", 19, "хостес"),
               ("Ерементий", 34, "сантехник"),
               ("Алекс", 30, "килер")
]

#выполнить несколько
cursor.executemany("""
INSERT INTO workers (name, age,profession)
VALUES (?, ?, ?)
""",new_workers)

connection.commit() # применить изменения

cursor.execute("SELECT * FROM workers") # выполнить запрос
rows = cursor.fetchall() # получить все
for row in rows:
    print(row)

cursor.close() # закрыть доступ

