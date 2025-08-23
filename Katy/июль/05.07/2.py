#создать класс дом
#две характеристики - колво комнат и цвет дома
# 2 действия - покрасить дом в новый цвет 2 - добавить новую комнату

class dom:
    def __init__(self):
        self.cout = 2
        self.color = "red"

    def chenge_color(self, new_color):
        self.color = new_color
    
    def add_room(self):
        self.cout += 1

new_dom = dom()
new_dom.add_room()

new_dom.chenge_color("Оранжевый")

print(new_dom.cout)
print(new_dom.color)





    