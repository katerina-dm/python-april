import sqlite3

with sqlite3.connect(r"Katy\avqyst\24.08\school.db") as connection:
    cursor = connection.cursor()
    cursor.execute(''' 
    SELECT autor, COUNT(id)
    FROM books
    GROUP BY autor
    ORDER BY COUNT (id) DESC
''')
    
    rows = cursor.fetchall()
    for row in rows:
        print(*row)