# numbers = [1,2,3]
# iterator = iter(numbers)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#print(iterator[2])   # list_terator  не имеет такого подхода. Итератор позволяет навигироваться по коллекции
# for i in numbers:
#     print(i)
# while True:                # фактическая реализация цикла for
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break
# print(3   in iterator)
# print(3   in iterator) # почему 2 раз Фалсе ? Итератор запомнил состояние в 1 принте
###################################################
# class MyIterator:
#     def __init__(self,collection):
#         self.collection = collection
#         self.cursor = -1
#
#     def __next__(self):
#         if self.cursor +1 >=len(self.collection):
#             raise  StopIteration
#         self.cursor +=1
#         return self.collection[self.cursor]
#
#     def __iter__(self):
#         return self
#
#
# if __name__ == "__main__":
#     iterator = MyIterator([1,2,3])
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # for i in iterator:
    #       print(i)
#####################################
## Генераторные выражения. Генератор
# def countdown(n):
#     while n> 0:
#         yield n
#         n -= 1

# generator = countdown(5)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(range(5))
# x = range(5)
# for i in x:
#     print(i)
###################################
#### функция lambda
# res = lambda x,y:x + y
# print(res(5,4))
# res2=(lambda x,y:x+y)(1,3)
# print(res2)
#
# def plu(x,y):
#     return x+y
# print(plu(1,2))
# отфильтровать Лямбда
# my_list = [1,2,4,8.1, "1",None,-129]
# print((lambda x:'OK' if any(x) else "Nok")(my_list) )
# print((lambda x:'OK' if all(x) else "Nok")(my_list) )
#########################################
##### Функции высшего порядка
def function(x):
    return x**2

def func(func,x):
    return func(x)+ func(x)
print(func(function,5))
