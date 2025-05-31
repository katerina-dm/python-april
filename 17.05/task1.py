#posts - список
posts = [
    {"likes": 5, "comments":3, "reposts":1},
    {"comments":4, "reposts":2},
    {"likes": 2},
    {"likes": 3, "comments":1, "reposts":1},
    {"likes": 10, "comments":50, "reposts":5},
]
#total_likes - переменная
#выводим сколько лайков
 # 1 вариант try и except 
 # 2 вариант метод словарей  i.get
 
total_likes = 0
for i in posts:
    total_likes += i.get("likes",-2)  
    #try:
        #total_likes += i["likes"]
    #except:
        #total_likes -= 2 

#-выводим сколько лайков
print(total_likes) 