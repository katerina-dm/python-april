#записать в файл task2.txt предпоследнюю строчку из _writelines  т.е 9 цифра

fl = open("_writelines.txt", "r", encoding="utf-8") # прочитали файл
lst = fl.readlines()[-2] #записали файл с 9 цифрой
fl.close()

fl = open("task2.txt", "w", encoding="utf-8") #перезаписали файл 
fl.writelines(lst)
fl.close()