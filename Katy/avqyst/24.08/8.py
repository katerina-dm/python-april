
import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\24.08\school.db") # подключили
cursor = connection.cursor() # создали активное подключение

cursor.execute('''
    INSERT INTO wallets ("teacher_id", "balance", "is_active")
    VALUES (1, 100, 1), (2, 100, 1),(3, 100, 1)       
''')     

connection.commit()

cursor.execute("SELECT * FROM wallets") 
rows = cursor.fetchall() 
for row in rows:
    print(row)

cursor.close() 