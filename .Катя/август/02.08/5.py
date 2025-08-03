import json

file_name = ""

musicians = {
    'Linkin Park' : ["Reanimation", 'Hybrid Theory'],
    'Rammstain' : ['Mutter', "Zeit"], 
    "Мияги" : ["Ямакаси", "Бастер Китон"] 
     }

def show_menu():
    print("Выберите операцию: ")
    print("0 - Загрузить данные из файла")
    print("1 - Выбрать групппу")
    print("2 - добавить группу")
    print("3 - удалить группу")
    print("4 - Сохранить изменения")
    print("5 - выход")

while True:
    show_menu()
    choise = int(input())
    if choise == 0:
        file_name = input("Введите название файла для загрузки:\n")
        try:
              with open(file_name, "r", encoding="utf-8") as fl:
                  musicians = json.load(fl)
              print(f'Файл с именем {file_name} успешно загружен!')

        except FileNotFoundError:
            answer = input('Файл не найден, создать пустой каталог? (да/нет): \n ')
            if answer.lower().strip() == "да":
                with open(file_name, "w", encoding="utf-8") as fl:
                  json.dump(musicians, fl)
                print(f'Файл с именем {file_name} успешно создан')
        except Exception as e:
            print(F"произошла непредвиденная ошибка: {e}")


    elif choise == 1:
        group = input("Введите название группы: ")
        if musicians.get(group, None) is not None:
          print(musicians.get(group, None))
        else:
          print(f"Группа {group} нет в каталоге") 

    elif choise == 2:
       group_for_add = input("Введите название группы для добавления: ") 
       if musicians.get(group_for_add, None) is not None:
           print(f"Группа {group_for_add} уже есть в каталоге")
       else:
            musicians[group_for_add] = []
            print(f"Группа {group_for_add} уже есть в каталоге")
            answer = input("Хотите добавить альбомы к групп? (Да/Нет: ")
            if answer.lower().strip() == "да":
                albums = input("Введите одно или несколько названий альбомов через запятую:\n" )
                if albums.isspace():
                    print("Строка пуста, альбомы не добавлены")
                else:
                    musicians[group_for_add] = [x.strip().capitalize() for x in albums.split(",")]
                    print(f"для {group_for_add} добавлены альбомы: {musicians[group_for_add]}")


    elif choise == 3:
        group_for_del = input("Введите название группы для удаления: ")
        try:
            musicians.pop(group_for_del)
            print(f"Группа{group_for_del} успешно удалена")
        except:
            print("Такой группы нет в каталоге")

    elif choise == 4:
        if not file_name:
            answer = input('Не выбран файл для сохранения,создать новый файл? (да/нет): \n ')
            if answer.lower().strip() == "да":
                file_name = input("Введите название файла для сохранения:\n")

            else:
                print("Изменения не сохранены! ")
                continue    
        with open(file_name, "w", encoding="utf-8") as fl:
            json.dump(musicians, fl)
        print(f'Все изменения успешно сохранены в {file_name}!')



    elif choise == 5:
        print("Выходим из программы")
        break
    else:
        print("Введена неккоректная команда") 

    input("Нажмите для продолжения")
