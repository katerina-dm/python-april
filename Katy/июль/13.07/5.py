
# с помощью функциии
def sum_n(a,b):
    return a + b

print(sum_n(1,5))

#тоже самое только через класс
class Sum_c:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self, *args, **kwds): #это функция встроена, *args - любое колво аргументов
        return self.a + self.b
    
s = Sum_c(1,5)
print(s())

print(callable(int))