# numbers = [1,2,3,4,5]
# print(numbers)
# numbers[1]=777 # замена 2 на 777 в списке
# print(numbers)
# просчет количества элементов в списке
# numbers = [1,2,3,4,5]
# teachers = ["Semen","Daniil","Ivan"]
# print(len(numbers))
# print(len(teachers))
# print(teachers)
#############################
#in в списках, смотрим какойто элемент есть ли в списках или нет
# names = ["Semen","Daniil","Ivan"]
# print('Semen' in names)
# print("Givi" not in names)
#####################################
#срезы в списках
# numbers =[2,4,6,8,10]
# print(numbers[1:3])
# print(numbers[2:5])
########################
# #функции sum() и min(), и max()
# a= [4,4,4,4]
# print(sum(a))
#####################
#распаковка списка
# a=["привет","как","дела","?","?"]
# print(*a)
#####################################
#нахождение и сумма минимального и максимального элемента в списке
# numbers = [200.33,5.4423,100.23, 100.99]
# minimum =min(numbers)
# maximum =max(numbers)
# print(f'Сумма минимального числа и максимального будет: {minimum+maximum}')
#####################################
#среднее арифметическое в списке
# numbers= [4,66,22,666,11,66,22,88,99,11,666,555]
# print(sum(numbers)/len(numbers))
######################################
#методы списка
#добавление элемента в список
# my_list = [1,2,3,4,5]
# my_list.append(777)
# print(my_list)
#########################
#добавление списка в список методом append(кладет целый список). Метод extend( кладет эдементы в существующий список
# my_list = [1,2,3,4,5]
# my_list.append([777,999,333,666,444])
# my_list2 = [1,2,3,4,5]
# my_list2.extend([777,999,333,666,444])
# print(my_list)
# print(my_list2)
# пример с строками и этими методами
# names = ["Anton","Vasili1","Ivan","Igor"]
# names.append(["Veneamin"])
# names2 = ["Anton","Vasili1","Ivan","Igor"]
# names2.extend("Veniamin")
# print(names)
# print(names2)
#############################
# метод split для разделения строк
# my_str = "Ехал Грека через реку"
# words = my_str.split()
# print(words)
##################
#
# my_str = ['Ехал', 'Грека', 'через' ,'реку']
# list_to_str = "!".join(my_str)
# print(list_to_str)
############################################
#уберание элемента из списка del
# my_list = ['Ехал', 'Грека', 'через' ,'реку']
# del my_list[-1]
# print(my_list)
############################################
# добавление элемента в список insert  в определенное место
# names = ["Anton","Vasili1","Ivan","Igor"]
# names.insert(1,'Veneamin')
# print(names)
#########################################################
# # узнать на каком месте находится элемент большого списка index
# names = ['Anton', 'Veneamin', 'Vasili1', 'Ivan', 'Igor']
# position = names.index("Igor")
# print(position)
##########################################################
#  метод pop узнать по номеру элемента, что находится. Метод забирает из списка элемент. ОН ВЫДЕРГИВАЕТ ЕГО
# names = ['Anton', 'Veneamin', 'Vasili1', 'Ivan', 'Igor']
# name = names.pop(-1)
# print(name)
# print(names)
#############################
# метод count подсчет одинаковых элементов в списке
# names = ['Anton','Ivan', 'Veneamin', 'Vasili1', 'Ivan','Anton', 'Igor','Anton']
# name = names.count('Anton')
# print(name)
#############################################
# так же подсчет с помощью цикла одинаковых элементов для примера
# names = ['Anton','Ivan', 'Veneamin', 'Vasili1', 'Ivan','Anton', 'Igor','Anton']
# count = 0
# for name in names:
#     if name == 'Anton':
#         count  +=1
# print(count)
###############################################
# метод для переварачивания списка reverse
# names = ['Anton','Ivan', 'Veneamin', 'Vasili1', 'Ivan','Anton', 'Igor','Anton']
# names.reverse()
# print(names)
######################
# метод clear для очистки списка. Делает пустой список
# names = ['Anton','Ivan', 'Veneamin', 'Vasili1', 'Ivan','Anton', 'Igor','Anton']
# names.clear()
# print(names)
######################################################
# копирование списка
# names =["Dania",'Alexander']
# names_v2 = names.copy()
# names.append('Vladimir') добавляется в  один список
# print(names)
# print(names_v2)
# копирование списка. Если копируем список в списке, то элемент командой append  добавится в оба списка
# names =["Dania",'Alexander',[1,2,3]]
# names_v2 = names.copy()
# names[2].append(4) # добавляется в оба списка, потому что вложенный список
# print(names)
# print(names_v2)
#######################
#метод  remove  удаляент первое вхождение элемента в список
# names =["Dania",'Alexander','Alexander','Alexander','Alexander',[1,2,3]]
# names.remove('Alexander')
# print(names)
####################
#метод sort  соритрует список по возрастанию
# names = [9,-10,3,5,9,1,47,-6,38,225]
# names.sort()
# print(names)
# #сортировка от большего к меньшего
# names = [9,-10,3,5,9,1,47,-6,38,225]
# names.sort(reverse=True) # reverse  от большего  к меньшему
#print(names)
# gah = [0,1]*10
# print(gah)
#############################
#КОРТЕЖИ . ПОхожи на списки, но они не изменяемые.  У кортежа всего 2 метода: index и count
# my_tuple=tuple([9,-10,3,5,9,1,47,-6,38,225])
# nomer = my_tuple.index(1)
# print(my_tuple)
# print(nomer)
#################################
# как что-то добавить в КОРТЕЖ. СНАЧАЛА его делаем в список!! # это просто создает новый список а не изменяет кортеж
# my_tuple=tuple([9,-10,3,5,9,1,47,-6,38,225])
# my_tuple =list
# my_tuple.append([1])
# print(my_tuple)
##########################
#создать кортеж из одного элемента
# my_tuple = (1,)
# print(my_tuple)
############################
#В кортеже лежит список, в список добавляем значения
# my_tuple=(9,-10,3,[1,2,3])
# my_tuple[3].extend([5,5])
# print(my_tuple)

