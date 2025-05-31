capitals = {"Russia": "Moscow", "Creat Britan": "London", "Spain":"Madrid"}
print(capitals)
print(f"Столицей России является {capitals["Russia"]}")

#capitals = dict(Russia="Moscow", Creat_Britan= "London", Spain="Madrid")
#print(capitals)

#capitals = dict([("Russia","Moscow"), ("Creat Britan", "London"), ("Spain", "Madrid")])
#print(capitals)

#for i in capitals: #вывели ключи
    #print(i)

#for i in capitals: #вывели значение
    #print(capitals[i])

#либо
#for key in capitals: #вывели значение
    #print(capitals[key])

#for i in capitals: #вывели значение и ключ
    #print((i,capitals[i]))

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

for item in capitals.items():
    print(item)

for key, value in capitals.items():
    print(key, value)
