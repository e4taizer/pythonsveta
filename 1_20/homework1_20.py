##### задание №1
# def decorator_name(arg_type):
#     def actual_type(func):
#         def wrapper(*args):
#             for i in args:
#                 if not isinstance(i,arg_type):
#                     raise TypeError(f"В функции {func.__name__} все аргументы должны быть типа {arg_type.__name__}")
#
#             return func(*args)
#         return wrapper
#     return actual_type
#
#
#
#
# @decorator_name (arg_type=int)
# def function_name (x,y,z):
#     return x+y+z
# print(function_name(2,3,4))
# print(function_name(1,2.2))
#####################
# def square_result(func):
#     def wrapper(*args):
#         result = func(*args)
#         return result ** 2
#     return wrapper
# @square_result
# def cymm(x,y):
#     return x+y
# print(cymm(10,10))
######################
# def decorator_name(arg_type):
#     def actual_type(func):
#         def wrapper(*args):
#             for i in args:
#                 if isinstance(i,arg_type):
#                     continue
#                 else:
#                    raise TypeError(f"В функции {func.__name__} все аргументы должны быть типа {arg_type.__name__}")
#
#
#             return func(*args)
#         return wrapper
#     return actual_type
#
# @decorator_name (arg_type=int)
# def function_name (x,y,z):
#     return x+y+z
# print(function_name(2,3,4.2))
#print(function_name(1,2.2))
############################
# Задание №2 контекстный менедежер
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()  # Отступ: 4 пробела
        return self  # Отступ: 4 пробела, выровнен относительно предыдущей строки

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()  # Отступ: 4 пробела
        print(f"Время выполнения: {self.end - self.start:.5f} секунд")
with Timer() as t:
    print("e")