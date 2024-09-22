######################## СЛОВАРИ
# dictionary = {} # пустой словарь Словари не хешируются. Изменяемые объекты все не хешируются
# numbers = dict() #  так же пустой словарь только функцией dict
##############################
#numbers ={2:"two",4:"four","six":6}
#names_and_ages = {"Alex":21,"Marc":18,"Maria":22, 4:"fhor"}
#print(names_and_ages)
#names_and_ages = dict(Alex=31,Marc=18,Maria=22)
#print(names_and_ages)
#names_and_ages = dict({"Alex":31} , Marc=18, Maria=22)
#print(names_and_ages)
####################
#Создание словаря с повторяющимися ключами
# awesome_dict = {
#     "first_key":"first",
#     "second_key":2,
#     "first_key":1
# }
# print(awesome_dict)
########
# создание словаря из списка кортежей
# names_plus_ages =  [("Alex",31),("Marc",18),("Maria",22)]
# list_to_dict = dict(names_plus_ages)
# print(list_to_dict)
# склеивание списков zip()
# names =  ["Alex","Marc","Maria"]
# ages = [31,18,22]
# zipped_dict = dict(zip(names,ages))
# print(zipped_dict)
##############
# fromkeys()  метод. None - значение не определено!
# products = ("DSP","PPInfo","KION")
# value = 1,2
# new_dict = dict.fromkeys(products,value)
# print(new_dict)
#################################
# удаление элеметов
# dict.pop(key,[,default]) или dict.popitem() это извлечение данных из словаря,
#позволяющее сохранить значения в отдельную переменнную и использовать в дальнейшем
#удаление через del.Полностью удаляет из словаря
# work_plases_spb = {
#     85: "Рабочий стол с докстанцией и монитором",
#     200:" Рабочее место",
#     202:"Рабочее место",
#     151:"Переговорка"
# }
# del work_plases_spb[202]
# del work_plases_spb[202]
# print(work_plases_spb)
#### экстрация через pop
# work_plases_spb = {
#     85: "Рабочий стол с докстанцией и монитором",
#     200:" Рабочее место",
#     202:"Рабочее место",
#     151:"Переговорка"
#                   }
# booked_place = work_plases_spb.pop(200)
# print(work_plases_spb.pop(200, "Рабочее место уже забронировано"))
# print(work_plases_spb)
# print(booked_place)
############
#Извлечение элементов  popitem() всегда последний элемент словаря выкидывает
# work_plases_spb = {
#     85: "Рабочий стол с докстанцией и монитором",
#     200:" Рабочее место",
#     202:"Рабочее место",
#     151:"Переговорка"
#                   }
# work_plases_spb.popitem()
# print(work_plases_spb)
###############
#Функции словарей
# work_plases_spb = {
#     85.1: "Рабочий стол с докстанцией и монитором",
#     200.111:" Рабочее место",
#     202:"Рабочее место",
#     151:"Переговорка"
#                   }
# print("Длина словаря составляет", len(work_plases_spb), "объекта")
# print(min(work_plases_spb))
# print(sum(work_plases_spb))
##########
#Метод copy() и deepcopy()
# work_places_spb = {
#     85: "Рабочий стол с докстанцией и монитором",
#     200:" Рабочее место",
#     202:"Рабочее место",
#     151:"Переговорка"
#                  }
# new_work_places = work_places_spb # так лучше не делать :)
# new_work_places[200] = "Рабочее место с кофемашиной"
# print(work_places_spb)
# print (new_work_places)
###
# work_places_spb = {
#     85: "Рабочий стол с докстанцией и монитором",
#     200:" Рабочее место",
#     202:"Рабочее место",
#     151:["Переговорка","Стулья","Стол","Чайник"
#                  }
# new_work_places = work_places_spb.copy()
# new_work_places[200] = "Рабочее место с кофемашиной"
# print(work_places_spb)
# print (new_work_places)
###
# meetings_room = ["Переговорка","Стулья","Стол","Чайник"]
# work_places_spb = {
#     85: "Рабочий стол с докстанцией и монитором",
#     200:" Рабочее место",
#     202:"Рабочее место",
#     151: meetings_room
# }
# new_work_places = work_places_spb.copy()
# new_work_places[200] = "Рабочее место с кофемашиной"
# meetings_room.remove("Чайник")
# print(work_places_spb)
# print (new_work_places)
##
# import copy
#
# meetings_room = ["Переговорка","Стулья","Стол","Чайник"]
# work_places_spb = {
#     85: "Рабочий стол с докстанцией и монитором",
#     200:" Рабочее место",
#     202:"Рабочее место",
#     151: meetings_room
# }
# new_work_places = copy.deepcopy(work_places_spb)
# new_work_places[200] = "Рабочее место с кофемашиной"
# meetings_room.remove("Чайник")
# print(work_places_spb)
# print (new_work_places)
##############################################
# как проверить есть ли значение в словаре метод values
# meetings_room = ["Переговорка","Стулья","Стол","Чайник"]
# work_places_spb = {
#     85: "Рабочий стол с докстанцией и монитором",
#     200:" Рабочее место",
#     202:"Рабочее место",
#     151: meetings_room
# }
# print("Рабочее место" in work_places_spb.values())
# #print(work_places_spb.values())
# for key in work_places_spb.keys(): # for key in work_places_spb.values():
#     print(key)
###
# meetings_room = ["Переговорка","Стулья","Стол","Чайник"]
# work_places_spb = {
#     85: "Рабочий стол с докстанцией и монитором",
#     200:" Рабочее место",
#     202:"Рабочее место",
#     151: meetings_room
# }
# print("Рабочее место" in work_places_spb.values())
# for key, values in work_places_spb.items():
#     print(key,values)
#######################
# Изменение значения в словаре
# shopping_list_and_cash = {
#     "fruits": ("peaches","apples","oranges"),
#     "meat": ["onions","potatoes","cabbages"],
#     "balance_usd":85
# }
# shopping_list_and_cash["balance_usd"] = 100
# shopping_list_and_cash["meat"][1] = "lettuce"
# print(shopping_list_and_cash)
###############################
#как поменять ключ в словаре - Никак, но есть лайфхаки
# shopping_list_and_cash = {
#     "fruits": ("peaches","apples","oranges"),
#     "meat": ["onions","potatoes","cabbages"],
#     "balance_usd":85
# }
# temporary_item = shopping_list_and_cash.pop("meat")
# print(temporary_item)
# print(shopping_list_and_cash)
# shopping_list_and_cash["vegetables"] = temporary_item
# print(shopping_list_and_cash)
##############
# распаковка словарей
# dict1 = {"a":1,"b":2}
# dict2 = {"c":3,"d":4}
# dict3 = {"a":5,"c":6}
# combined_dict = {**dict1,**dict2,**dict3}
# print(combined_dict)
#####################
#словари в словарях
# nested_dict ={
#     "key1":{
#         "nested_key1":"Hello",
#         "nested_key2": "Hello",
#         "nested_key2": "Apple"
#     },
#     "key2":{
#         1:"car",
#         2:"bike",
#         3:"jet"
#     },
#     "key3":[1,2,3]
# }