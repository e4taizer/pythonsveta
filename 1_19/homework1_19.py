#### задание №1
# string_numbers = [1,100,"python",444,"iterator",6,3,"and",999,"generator"]
# def only_str(n,condition):
#     for item in n:
#         if isinstance(item,condition):
#            yield  item
#
#
#
#
# filter_list = list(only_str(string_numbers,str))
# print(filter_list)
######################################
#задание №2
# string_numbers = [1,100,"python",444,"iterator",6,3,"and",999,"generator"]
# #only_int = list(filter(lambda x:isinstance(x,str),string_numbers))
# #only_int = list(filter(lambda x:isinstance(x,str) and len(x)>5,string_numbers))
# only_int = list(filter(lambda x:isinstance(x,int) and x%2,string_numbers))
# print(only_int)
##################################
#задание №3
# c проходом 2 раза по массиву
# class Myiterator:
#     def __init__(self,massive):
#         self.massive = massive
#         self.cursor = -1
#         self.repeated = False #  флаг который смотрит  количество раз, на 1 проходе фалсе, на 2 трю и  Стоп итерейшен
#     def __next__(self):
#         if self.cursor +1 >=len(self.massive) and self.repeated:
#             raise StopIteration
#         if self.cursor + 1 >= len(self.massive):
#             self.cursor = -1
#             self.repeated = True
#
#
#         self.cursor +=1
#         return (self.massive[self.cursor]+2)**2
#     def __iter__(self):
#         return self
#
#
# if __name__ == "__main__":
#     iterator = Myiterator([1,2,3])
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#######################
# с проходом 3 раза по массиву
# c проходом 2 раза по массиву
class Myiterator:
    def __init__(self,massive):
        self.massive = massive
        self.cursor = -1
        self.repeated_count = 0
    def __next__(self):
        if self.cursor +1 >=len(self.massive):
            self.cursor = -1
            self.repeated_count += 1
        if self.repeated_count >=5:
            raise StopIteration



        self.cursor +=1
        return (self.massive[self.cursor]+2)**2
    def __iter__(self):
        return self


if __name__ == "__main__":
    iterator = Myiterator([1,2])
print(list(iterator))







