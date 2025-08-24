# Таблица - wallets
# Поля - 
# # id - первичный ключ
#  teacher_id - связь с таблицей teachers
# balance - число не может быть 0
# is_active - булево значение

import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\24.08\school.db") # подключили
cursor = connection.cursor() # создали активное подключение

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute('''
CREATE TABLE IF NOT EXISTS wallets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER,
    balance INTEGER  NOT NULL CHECK (balance >= 0),
    is_active INTEGER CHECK (is_active IN (0, 1)),
    FOREIGN  KEY (teacher_id) REFERENCES teachers (id))
    ''')


connection.commit()