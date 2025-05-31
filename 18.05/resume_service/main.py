# импортиуем файл parser

from parser import parse_resume_data
from html_create import generate_html, save_html_to_file



def main():

    resume_faile_name ="resume_data.txt"
    


    print("Читаем парсинг файл....")
    resume_data =parse_resume_data(resume_faile_name)
    print(resume_data)
    if resume_data:
        html_filename = "resume.html"

        print("Подготавливаем html страницу...")
        html_data = generate_html(resume_data)
        print(f"Созраняем страницу html в файл {html_filename}...")
        save_html_to_file(html_data, html_filename)
        print("Процесс завершен успешно!")
        
    else:
        print(f"Неудалось обработать данные из {resume_faile_name}")



if __name__ == "__main__" :
    main()