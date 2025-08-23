#множественное нследование
class Parent1:
    def say(self):
        print("Hello fron Parent1")

class Parent2:
    def sleep(self):
        print("Zzzzz")

class Child(Parent1, Parent2):
    pass

c = Child()

c.say()
c.sleep()