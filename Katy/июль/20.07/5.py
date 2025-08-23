#множественное нследование
class Parent1:
    def say(self):
        print("Hello fron Parent1")

class Parent2:
    def sleep(self):
        print("Zzzzz")
    def say(self):
        print("Hello fron Parent2")

class Child(Parent2, Parent1):
    pass

c = Child()

c.say()
c.sleep()