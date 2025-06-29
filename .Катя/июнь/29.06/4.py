class Auto:
    def __init__(self,form ,color,power ):
        self.form = form
        self.color = color
        self.power = power
        self.producer = "Cermany"

#как сделать атрибут приватным, __ добавляем
#для того чтоб вывести атрибут
#высчитываем налог, т.е добавляем
        if power <= 150:
            self.__tax = 5000
        elif power > 150 and power <=200:
            self.__tax = 15000
        else:
           self.__tax = 50000

#для того чтоб вывести атрибут, его создаем
    def show_tax(self):
        return self.__tax
        

bmw = Auto("седан", "черный", 200)
print(bmw.color)
print(bmw.show_tax())

