from dotenv import load_dotenv
import os

load_dotenv() #вызываем для того чтоб загрузить env

api_key = os.getenv("API_KEY")
login = os.getenv("LOGIN", "username") 
password = os.getenv("PASSWORD", "password")

print(api_key)
print(login)
print(password)