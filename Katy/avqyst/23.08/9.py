import sqlite3

connection = sqlite3.connect(r"Katy\avqyst\23.08\school.db") # подключили
cursor = connection.cursor() # создали активное подключение

def add_new_worker(name, age, profession):
    cursor.execute("""
    INSERT INTO workers (name, age,profession)
    VALUES (?, ?, ?)
    """,(name, age, profession))

    connection.commit() # применить изменения


def delete_worker(worker_id): #функция удаления работников
    cursor.execute("DELETE FROM workers WHERE id = ?", (worker_id,))
    connection.commit() # применить изменения


def show_workers(): #функция отоброжения работников
    cursor.execute("SELECT * FROM workers") # выполнить запрос
    rows = cursor.fetchall() # получить все

    for row in rows:
        print(row)


def print_menu():
    print("1 - добавить нового работника")
    print("2 - удалить работника по его id")
    print("3 - показать всех работников")
    print("4 - выход")

while True:
    print_menu()
    choice = input ("Введите номер команды: ")
    try:
        choice = int(choice)
    except:
        print("Введены некорректные данные!")
        input("Нажмите любую кнопку для продолжения")
        continue

    if choice == 1:
        name = input("Введите имя работника: ")
        age = int(input("Введите возраст работника: "))
        profession = input("Введите профессию работника: ")
        
        add_new_worker(name, age, profession)
        print("Операция успешно выполнена!")


    elif choice == 2:
        id = int(input("ВВедите номер id: "))
        delete_worker(id)
        print("Операция успешно выполнена!")

    elif choice == 3:
        show_workers()

    elif choice == 4:
        break

    else:
        print("Данная команда отсутствует")
    input("Нажмите любую кнопку для продолжения")
