autos =("bmw", "audi", "ford", "tesla")
print(autos)

user_choice, rename = input("Введите марку авто и слово для замены").split()
count = autos.count(user_choice)


#второй вариант
def is_equal(x):
    if x == user_choice:
        return rename
    else:
        return x
    
if count:
    #autos = tuple(map(lambda x: rename if  x==user_choice else x, autos)) # через map заменили обьект 
    autos = tuple(map(is_equal, autos)) #второй вариант

print(autos)