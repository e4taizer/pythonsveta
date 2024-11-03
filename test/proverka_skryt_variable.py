import os
from dotenv import load_dotenv
load_dotenv()
user_login = os.getenv("22fefefe") #так делать в коде не нужно(передовать пароли)
user_pass = os.getenv("22ffef")  #
print(f"Юзер с логином {user_login} использовал пароль {user_pass}")