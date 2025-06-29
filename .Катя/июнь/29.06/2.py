class Auto:
    def __init__(self,form ,color,power ):
        self.form = form
        self.color = color
        self.power = power
#заполняем характеристики
bmw = Auto("седан", "черный", 200)

print(bmw.color)