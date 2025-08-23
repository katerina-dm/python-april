peoples = 20

def print_Pposad():
    global peoples
    peoples = 80
    print(f"Численность населения в Павловском Посаде {peoples} тысяч человек")#f форматированная строка


def print_Noginsk():
    peoples = 102
    print(f"Численность населения в Ногинске {peoples} тысяч человек")

print(peoples)
print_Pposad()
print_Noginsk()
print(peoples)