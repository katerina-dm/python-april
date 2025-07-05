# класс - Dun
# count - количество выстрелов. В начале равно 0
# метод - shoot - при вызове пишет "Pif" 
# метод - shootc.count - возвращает нам количество выстрелов

class Dun:
    def __init__(self):
        self.count = 0
    def shcoot(self):
        self.count += 1
        print("Pif")

    def shootc_count(self):
        return self.shootc_count
    
new_dun = Dun()
new_dun.shcoot()
print(new_dun.count)




