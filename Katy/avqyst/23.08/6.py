import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\23.08\school.db") # подключили
cursor = connection.cursor() # создали активное подключение
print("База данных усмешно подключена!")

new_woker = ("Павел", 55, "Сварщик")

cursor.execute("""
INSERT INTO workers (name, age,profession)
VALUES (?, ?, ?)
""",new_woker)

connection.commit() # применить изменения

cursor.execute("SELECT * FROM workers") # выполнить запрос
rows = cursor.fetchall() # получить все
for row in rows:
    print(row)

cursor.close() # закрыть доступ

