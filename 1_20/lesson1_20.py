#### Декораторы . Декоратор это паттерн!
# def my_dec (func):
#     def wrapper():
#         print("before")
#         func()      # идет выполнение def say_hello
#         print("after")
#     return  wrapper
# @my_dec
# def say_hello():
#     print("hello!")
# say_hello()
##########################
# from datetime import datetime
# def time(function):
#     def wrapper(*args,**kwargs):
#         start= datetime.now()
#         result = function(*args,**kwargs)
#         print("function %s time:" % function.__name__.upper(),datetime.now()-start)
#         print(args)
#         print(kwargs)
#         return result
#     return wrapper
# @time
# def one(n):
#     l =list()
#     for i in range(n**4):
#         if i % 2 == 0:
#             l.append(i)
#     return l
# @time
# def two(n):
#     l =[x for x in range(n**4) if x%2 == 0]
#     return l
#
# one(5)
# two(5)
# ##############################################
# #контекстный менеджер

