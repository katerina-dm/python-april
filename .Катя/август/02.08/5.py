
musicians = {
    'Linkin Park' : ["Reanimation", 'Hybrid Theory'],
    'Rammstain' : ['Mutter', "Zeit"], 
    "Мияги" : ["Ямакаси", "Бастер Китон"] 
     }

def show_menu():
    print("Выберите операцию: ")
    print("1 - Выбрать групппу")
    print("2 - добавить группу")
    print("3 - удалить группу")
    print("4 - выход")

while True:
    show_menu()
    choise = int(input())
    if choise == 1:
        group_for_add = input("Введите название группы")
        if musicians.get("group_for_add", None) is not None:
          print(musicians.get("group_for_add", None))
        else:
          print(f"Группа {group_for_add} нет в каталоге") 

    elif choise == 2:
       group_for_add = input("Введите название группы для добавления") 
       if musicians.get("group_for_add", None) is not None:
           print(f"Группа {group_for_add} уже есть в каталоге")
       else:
            musicians[group_for_add] = []
            print(f"Группа {group_for_add} уже есть в каталоге")


    elif choise == 3:
        group_for_del = input("Введите название группы для удаления")
        try:
            musicians.pop(group_for_del)
            print(f"Группа{group_for_del} успешно удалена")
        except:
            print("Такой группы нет в каталоге")


    elif choise == 4:
        print("Выходим из программы")
        break
    else:
        print("Введена неккоректная команда") 

    input("Нажмите для продолжения")