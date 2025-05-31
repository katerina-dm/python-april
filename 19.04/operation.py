# операции над множеством. Эти операции не изменяли исходное множество

st1= {0,1,2,3,4,5,6}
st2 = {5,6,7,8,9}
print(st1)
print(st2)

#обьединение
#st3 = st1.union(st2) 
#print(st3) #записывается без повторов

#или
#st4 = st1 | st2 
#print(st4) 

#пересечение
#st3 = st1.intersection(st2)
#print(st3) # схранилось 5,6 потому что они повторились

#или
#st4 = st1 & st2
#print(st4)

#разность
#st3 = st1.difference(st2)
#print(st3) 

#или
#st4 = st1 - st2 # st2 - st1 неравно  
#print(st4)

#Симметричная разность
st3 = st1.symmetric_difference(st2)
print(st3) #повторяющие значения не сохранились

#или
st4 = st1 ^ st2 # st1 ^ st2 одинаково
print(st4)
