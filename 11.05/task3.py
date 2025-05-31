rd = open("scores.txt", "r", encoding="utf-8")  #rd считываем файл
wr = open("task3.txt", "w", encoding="utf-8")  #wr записываем

line = rd.readline()
while line !="":
    # line - "Петров 3 5 5 4 5\n"
    # вытаскиваем цыфры
    new_line = line.strip().split()
    # new_line - [ "Петров", "3", "5", "5", "4", "5"] должно так получится
    awg = [int(i) for i in new_line[1:]] # записали то что должно получиться за исключением первого элемента
    # awg - [ "3", "5", "5", "4", "5"] #то что получили
    awg =sum(awg)/len(awg)
    wr.write(f"{new_line[0]} {awg}\n") 

    line = rd.readline()

rd.close()
wr.close()




