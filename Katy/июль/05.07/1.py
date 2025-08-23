class Zanachka:
    def __init__(self):
        self.__cout = 0
 
 #положить ,view_cash - метод 
    def view_cash(self):
        return self.__cout

#добавить
    def add_cash(self, add_to_cash):
        if add_to_cash >= 0:
            self.__cout += add_to_cash
        

#изьять
    def withdraw_cash(self, withdra_to_cash):
        if self.__cout >= withdra_to_cash:
            self.__cout -= withdra_to_cash
        else:
            print("В заначке недостаточно средств")

#создаем новую переменную
aleksandr = Zanachka() 

print(aleksandr.view_cash())

#добавляем
aleksandr.add_cash(50_000)
print(aleksandr.view_cash())

aleksandr.withdraw_cash(1000)
print(aleksandr.view_cash())

aleksandr.withdraw_cash(60000)
print(aleksandr.view_cash())

aleksandr.__cout = 1_000_000
print(aleksandr.view_cash())