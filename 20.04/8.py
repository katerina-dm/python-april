files_list = ["photo.png",
              "photo1.png",
              "photo.jpeg",
              "photo.txt",
              "new_year.rar",
              "2025.docx",
              "Tree.PNG",
              "github.git",
              ".evn",
              "bebepng",
              "tree.Png"
               ]

st = {i.lower() for i in files_list if ".png" in i.lower()} #генератор строки

for i in st:
    print(i)

