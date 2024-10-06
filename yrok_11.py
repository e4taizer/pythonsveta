############ функции
# def print_hello():
#   print("Hello")
# print_hello()
############
# def print_kvadrat():
#  for _ in range(5):
#     print('*'*5)
# print_kvadrat()
#######пустая функция заглушка пасс
# def empty():
#     pass
################ заданный параметр
# def print_kvadrat(size, count=3) :
#     for _ in range(count):
#         for _ in range(size):
#            print('*'*size)
#
# print_kvadrat(1)
## нельзя использовать изменяемый тип данных в параметрах по умолчанию!!
# def my_func(x="My",y='love'):
# #     print(x,y)
# # my_func(y="ne naebesh")
#################### список внитри функции создание
# def my_func(num, lst=None):
#     if lst is None:
#         lst =[]
#     lst.append(num)
#     print(lst)
# my_func([6,2],[8])
##### использование  позиционных и именнованных вместе в функциях,сначала передается похиционные
# потом именнованые
# def my_func(x,y,z):
#     print(x,y,z)
# my_func(4,z=5,y=6)
###### если не знаем сколько будет позиционных аргументов *args
# def my_func(*args):
#     for item in args:
#         print(item)
#     print(args)
# my_func(1,2,3,4,5)
#### kwargs  аргумент переменной длины. С именноваными аргументами
# def my_func(**kwargs):
#  for key,value in kwargs.items():
#      print(key,value)
# my_func(one="monday",two="sunday")
############ если добавляем значение в изменый тип данных, значение меняется так же  в переменной
# num =[42,43,44]
# def some_func(n):
#     n[0]=0
#     print(n)
# some_func(num)
# print(num)
############## функция return/ Если не использховать ретерн то функция выведет Noone
# def  my_func(num1,num2):
#     result = num1*num2
#     return  result
# print(my_func(1,3)+my_func(5,8))
### Рекурсия. Функция вызывает саму себя
# my_list =[1,2, [3,4,[5,6]],7,[8,9]]
# # def my_func(lst):
# #     result= []
# #     for item in lst:
# #         if isinstance(item,list):
# #             result.extend(my_func(item))
# #         else:
# #             result.append(item)
# #
# #     return result
# # print(my_func(my_list))
# counter = 100
###########################
# def increment():
#     counter = 1
#     def inner(num):
#         nonlocal  counter
#         counter +=num
#         print(counter*2)
#     inner(counter)
# increment()
##################
#факториал фисла 3 == 3*2*1
# def count_fact(number:int) ->int:
#     result =1
#     for i in range(1,number+1):
#      result *= i
#     return result
# print(count_fact(5))
####### факториал решение рекурсивное
# def count_fac_rec(number:int) ->int:
#     if number ==0:
#         return 1
#     return number * count_fac_rec(number - 1)
#
#
# print(count_fac_rec(4))
