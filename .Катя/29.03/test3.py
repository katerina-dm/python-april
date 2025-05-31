def draw_figure(h,w): #название функции
    for i in range(h):
        for j in range(w):
            print(" * " , end="")
        print()
    print() #для отступа фигур

draw_figure(10,3) #h,w
draw_figure(4,7)
draw_figure(5,6)
