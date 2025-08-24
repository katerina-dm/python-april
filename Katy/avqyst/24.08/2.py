import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\24.08\school.db") # подключили
cursor = connection.cursor()

cursor.execute("SELECT * FROM books") #запросили полностью базу данных
d = cursor.description # с помощью этого получили название колонок

for i in d:
    print(i[0])

name_list = [i[0] for i in d]
print(name_list)
