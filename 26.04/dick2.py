capitals = {"Russia": "Moscow", "Creat Britan": "London", "Spain":"Madrid"}
capitals2 = {"Russia": "Moscow", "Creat Britan": "London", "Spain":"Madrid"}

if "Russia" in capitals:
    print(f'Столица России -{capitals['Russia']}')

print("Russia" in capitals)
print(capitals == capitals2)

print("Moscow" in capitals.values()) #проверяем есть ли Москва в строчке