#Пакеты и модули в пайтон.Базовые модули
# import sys
# print(sys.path)
# def tochki():
#     stroka = input("Введите текст:")
#     result = ''.join(
#         stroka[i] + '.' if stroka[i].isalpha() and i < len(stroka) - 1 and stroka[i + 1].isalpha() else stroka[i] for i
#         in range(len(stroka)))
#     print(result)
# tochki()
def add_dots(text):
    return ' '.join(['.'.join(i) for i in text.split()])[:-2] + '' + text.split()[-1][-1]
print (add_dots("hello World!!!!!"))