#readline - считываем одну строчку


fl = open("_readline.txt", "r", encoding="utf-8")

#print(fl.readline(), end="")
#print(fl.readline())

line = fl.readline()
while line != "":
    if line[0] == "7":
        print(line, end= "")
    line = fl.readline()
fl.close()