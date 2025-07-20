class Hero:
    def __init__(self,name,health):
        self.name = name
        self._health = health

#Создаем опиисние класса
    def __str__(self):
        return f"Герой {self.name}, Здоровье {self.health}"
#Добавить метод экземпляра
    def take_damage(self,damage):
        if damage > 0:
            print (f"{self.name} получил {damage} урона") 

        self.health -= damage
        if self.health <= 0:
            print (f"{self.name} ушел") 

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self,nhels):
        if nhels >= 0:
            self._health = nhels
        else:
            self._health = 0

            
    def is_alive(self):
        if self._health > 0:
            return True
        return False


hero1 = Hero("Арагорн", 100)
hero1.take_damage(25)
print(hero1)

hero2 = Hero("Гэндальф", 120)
print(f"Жив ли {hero2.name}? {hero2.is_alive}")
hero2.health = 50
print(hero2)

hero2.take_damage(150) 
print(hero2)
print(f"Жив ли {hero2.name}? {hero2.is_alive}")
