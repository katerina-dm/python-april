abs = {
    1: ".,!?",
    2: "АБВГ",
    3: "ДЕЖЗ",
    4: "ИЙЛЛ",
    5: "МНОП",
    6: "РСТУ",
    7: "ФХЦЧ",
    8: "ШЩЪЫ",
    8: "ЬЭЮЯ",
    0: " ",
}

s = input("Введите строку для кодировки:  ")#key и value 
for ch in s:
    for k,v in abs.items():
        if ch.upper() in v:
           print(str(k) * (v.index(ch.upper()) + 1), end= "")
        
