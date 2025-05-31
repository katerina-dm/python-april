fl = open("_writelines.txt", "r", encoding="utf-8")  # прочитали файл

lst = fl.readlines()[:: - 1] #перевернули файл
fl.close() #закрыть функцию, обязательно 

fl = open("task1.txt", "w", encoding="utf-8") #перезаписали файл
fl.writelines(lst)
fl.close()