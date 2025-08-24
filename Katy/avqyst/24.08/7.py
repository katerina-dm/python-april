import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\24.08\school.db") 
cursor = connection.cursor()

cursor.execute("SELECT * FROM wallets") 
d = cursor.description

for i in d:
    print(i[0])

connection.commit()