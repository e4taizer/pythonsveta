### Модуль ос в пайтон
# import os
# print("Начало кода тут:")
# os.chdir("..") # 2 точки в юник системах вернуться на уровень выше!
# print(os.getcwd()) # возвращает текущую рабочую директорию
##################
# import os
# print("Начало кода тут:")
# os.chdir("../pythonsveta") # смена директории на другую chdir()
# print(os.getcwd())
####### Вывод списка директорий и файлов
# import os
#
# print(os.listdir())
# print(os.listdir("../pythonsveta2")) # с указанием папки\директори список файлов папок
################### os.getenv() Можно спратать данные в коде. Выводи Noone
import os
# user_login = "test1234" #так делать в коде не нужно(передовать пароли)
# user_pass = "12345678"  #
# print(f"Юзер с логином {user_login} использовал пароль {user_pass}")
import os
import shutil

from dotenv import load_dotenv
# user_login = os.getenv("LOGIN") #так делать в коде не нужно(передовать пароли)
# user_pass = os.getenv("PASSWORD")  #
# print(f"Юзер с логином {user_login} использовал пароль {user_pass}")
###Создание директорий
#os.mkdir("./cool-dir") ## создание новой директории
#os.makedirs("./cool-dir1/another-dir") #создание вложенной директории
############## Переименование перемещение удаление
#  os.rename("calc.py","super_calc.py") # перемеинование файла
# os.replace("","")
# os.rmdir("") удаление директории
# оs.path.join()  склеивание путей

######################## Модуль shutil
# import os
#
# shutil.copytree("../pythonsveta/test","../pythonsveta/testcopy") # копирование директории
# shutil.rmtree("../pythonsveta/testcopy") # удаление папки\каталога по пути
# shutil.move("../pythonsveta2", "../pythonsveta/test") # перемещение файлов ! внимание файлы  аврезаются и вставляются
# , еслим перемещь файл в файл то будет перезаписывание кода !!
# shutil.copyfile("../","../") этот метод просто копирует без перезаписи и удаления
###################
# ФС функции\методы работы с ней
# f =open("example.txt","w")  открытие файла
# f.write("Hello World1!") перезапись данных в файле
# f.close() закрыть файл
#########################
# with open("example.txt","a+") as f: #правильное добавление  в файл через with.... as
#     f.write("Hello,Python!")
#чтение из файла метод read()\
 #with open("example.txt","a+") as f:
    # f.write("n\Hello,Python!")

# with open("example.txt")as f:
#      text =f.read()
#      part =f.read(5)
#      #print(text)
#      print(part)
################
# чтение из файла построчно
# with open("example.txt") as f:
#     for line in f:
#         print(line)
#########################
#Работа с курсором\кореткой tell()
# with open("example.txt") as f:
#     f.readline(10)
#     part =f.read(5)
#     print(part)
#     print(f.tell())
####################
#Работа с курсором\кореткой и сдвиг курсора seek()ааа

