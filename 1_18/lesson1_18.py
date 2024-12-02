###№№№№№№№№Декораторы
# class Rectangle:
#     count_rectangle_from_sqaure =0
#     def __init__(self,width,height):
#          self.width =width
#          self.height = height
#     @classmethod
#     def from_sqaure(cls,side):
#         cls.count_rectangle_from_sqaure +=1
#         return cls(side,side)
#
#
# rect = Rectangle.from_sqaure(4)
# print(rect)
# print(rect.count_rectangle_from_sqaure)
###  декоратор @staticmethod
# class Cat:
#       meow_count = 0
#
#
#       def __init__(self):
#           self.breed = "Уличный"
#
#
#       @staticmethod
#       def say(phrase):
#           return f"{phrase} meow!"
#
# print(Cat.say("I am cat"))
# print(Cat().say("I am instace cat"))
###########################################
# Инкапсуляция
#
# class Petowner:
#        def __init__(self):
#           self.__doc_number = 3414
#           self._doc_series = 3232323
#        def __print_int(self):
#            print(3)
#
# owner = Petowner()
#
# #print(owner._doc_series)
# print(owner._Petowner__doc_number) # способ вызова приватного метода
# owner._Petowner__print_int()
######################################
# class NewCat:
#
#     def __init__(self):
#         self.__paws_count =4
#     @property
#     def paws_count(self):
#         return self.__paws_count
#
#     def __validate_paws_count(self,count):
#         return  count > 0
#
#     @paws_count.setter
#     def paws_count(self,value):
#         if self.__validate_paws_count(value):
#             self.__paws_count = value
#         else:
#             raise ValueError("Ты пытаешься лишить котика лапок!")
#
# new_cat = NewCat()
# print(new_cat.paws_count)
# new_cat.paws_count = 3
# print(new_cat.paws_count)
# new_cat.paws_count = 4
# #new_cat.paws_count = 0
##########################практика @property
# class  UpdatePetOwner:
#     def __init__(self,fio,age,doc_number):
#         self.fio =fio
#         self.age= age
#         self.doc_number=doc_number
#
#     @property
#     def full_name(self):
#         return self.__fio
#     @full_name.setter
#     def full_name(self,value):
#         if type(value) is str:
#             self.__fio= value
#         else:
#             raise ValueError("ФИО должно быть строкой")
#
# pet_owner = UpdatePetOwner("Соколов А.В.",29,444)
# pet_owner.full_name ="Пупки Иван Иванович"
# print(pet_owner.full_name)
#####################
# вызов приватного метода через специальную конструкцию
# class Myclass:
#     def __init__(self):
#         self.__private_attribute = 42
#
#
# class MyNewClass(Myclass):
#     def __init__(self):
#         super().__init__()
#
#     def print_private_attribute(self):
#         print(self._Myclass__private_attribute)
#
# MyNewClass().print_private_attribute()
##############################################
#Магические методы __str__  #магичееский метод __getattribute__  __ssetattr_
# class Cat:
#     def __init__(self,name,age,breed):
#         self.name =name
#         self.age= age
#         self.breed = breed
#
#     def __str__(self):
#         return f"Я  кот {self.name}, мне {self.age} лет"
#
#     def __repr__(self):
#         return f'Cat("{self.name}", 8)'
#     # def __getattribute__(self, item):
#     #     if item =="breed":
#     #         return 'Это персональные данные кота'
#     #     else:
#     #         return object.__getattribute__(self,item)
#
#     def __getattr__(self, item):
#         return f"У кота нет такого свойства {item}"
#
#     def __setattr__(self, key, value):
#         if "tail" in key :
#             print(f"Хвост нельзя менять!")
#         else:
#             object.__setattr__(self,key,value)
#
# #
# # #cat_sam = Cat('Cэм',7)
# # # cat_string = str(cat_sam)
# # cat_repr= repr(cat_sam)
# # print(cat_string)
# # print(cat_repr)
# # second_cat_sam = eval(cat_repr)
# # print(second_cat_sam)
# # exec("b=2")
# # print(b)
# new_cat = Cat('Сэм',8,'Уличный')
# # # print(new_cat.breed)
# # # print(new_cat.second_name)
# # # print (new_cat.__dict__)
# # new_cat.tail = "пушистый"
# # new_cat.eye_color = "желтый"
# # print(new_cat.eye_color)
# # new_cat.__dict__['tail'] = "Пушистый"
# # print(new_cat.tail)
# ################################################## метод __add__
# class CatFamily:
#     def __init__(self):
#         self.cat_count = 0
#
#     def __add__ (self,other):
#         if isinstance(other,Cat):
#             self.cat_count +=1
#         else:
#             raise  ValueError("В семью можно добавить только кота")
#
#     def __eq__(self, other):
#         if isinstance(other,Cat):
#             return self.age == other.age
#         else:
#             raise ValueError("Это не кот")
#
#
# # family = CatFamily()
# # family +new_cat
# # print(family.cat_count)
# # #family+1
#
# old_cat = Cat('Барсик',8,'Шотландская')
# print(new_cat == old_cat)
# print(new_cat.age, old_cat.age)
############################################
class MyClass:
    def __init__(self):
        self._protected_attribute = 42
    def __getattr__(self,name):
        return f'Атрибут {name} не определен'
    def __setattr__(self, name, value):
        if name.startswith("_"):
            object.__setattr__(self,name,value)
        else:
            raise AttributeError("Не можем присвоить значение")

my_obj = MyClass()
my_obj.my_attribute = 100

