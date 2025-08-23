# создть класс Book
# Содержит 3 атрибута name, author, year
#Формат текста : "Буратино",Алексей Николаевич Толстой, 1999

class Book:
   def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

   def __str__(self):
        return f"Книга {self.name},Автор {self.author}, год издания {self.year}"

name =  Book("Буратино", "Алексей Николаевич Толстой", 1999)
print(name)


