import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\24.08\school.db") # подключили
connection.row_factory = sqlite3.Row 
cursor = connection.cursor()

cursor.execute("SELECT * FROM books") #запросили полностью базу данных
rows = cursor.fetchall() # получить все
data = [dict(row) for row in rows]

#for d in data:
    #print(d)

for row in rows:
    print(row["title"])

cursor.close() # закрыть доступ
