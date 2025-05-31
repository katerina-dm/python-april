#Модуль рандом, генерирует от 0 до 1, но 1 не включает

import random as r

#for i in range(5):
    #print(r.random())

#for i in range(5):
    #print(r.randrange(2,100,2)) # положительное от 0 до 100 например


#for i in range(5):
    #print(r.randrange(90,100)) #генерирует целое число, включаяя последнее


lst = [i for i in range(10)]
print(r.choice(lst)) 

print(r.sample(lst, 4))
