import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\24.08\school.db") # подключили
cursor = connection.cursor()

cursor.execute('''
    INSERT INTO books (title, autor, publish_date, page_value)
    VALUES ("Кубок огня","Джоан Роулинг","2005-12-12", 650)           
''')     

print(cursor.lastrowid) #id последней строки

connection.rollback()# Отмена действий ,если невыполняется неразделимая операция
connection.close() # полностью закрываем базу данных
