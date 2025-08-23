#__init__(self) - переменная которая ссылается на конретный обьект
class Auto:
    def __init__(self):
        self.form = "Седан"
        self.color = "Белый"
        self.power = 200

      

bmw = Auto()
#print(bmw.color) -  через точку обращаемся к атрибуту
print(bmw)
print(bmw.form)
print(bmw.color)
print(bmw.power)

#изменили один элемент
bmw.power = 250
print(bmw.power)


#добавили новый элемент,он со старыми характеристиками
audi = Auto()
print(audi.power)
