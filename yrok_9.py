############# множества

# my_tuple = 112211
# print(hash(my_tuple))
# my_tuple2 = (1,2,"hello")
# print(hash(my_tuple2))
# list1 = [1,2,3]
# string = "hello world"
# new_set = set(list1)
# new_set1 = set(string)
# print(new_set)
# print(new_set1)
#########################
# создание пустового множества
# i = set()
# print(type(i))
#####################
# znachenie = [1,True,(1,0)]
# for i in znachenie:
#     print(hash(i))
###############################
# Объединение множеств .union  |
# first_set = {1,2,3,4,5}
# second_set = {4,5,6,7,8}
# print(first_set.union(second_set))
# print(first_set | second_set)
##################################
# Пересечение множеств  intersection &
# first_set = {1,2,3,4,5}
# second_set = {4,5,6,7,8}
# print(first_set.intersection(second_set))
# print(first_set & second_set)
#######################################
# разность множеств. Порядок множест имеет значение. Идет вычитание.
# first_set = {1,2,3,4,5}
# second_set = {4,5,6,7,8}
# print(second_set - first_set)
# print(first_set.difference(second_set))
####################################################
#Симметрическая разность  ^
# first_set = {1,2,3,4,5}
# second_set = {4,5,6,7,8}
# print(first_set ^ second_set)
# print(second_set.symmetric_difference(first_set))
######################################################
# опретор in в множествах
# super_set = {1,'car',(1,2), True}
# print('car' in super_set)
# print(True not in super_set)
####################################
# как не выстрелить себе в колено множеством - что первое пришло, то и выведется при динамической типизации
# super_set = {1, "a", True}
# print(super_set)
# выведет {1,"a"}
# super_set = {True, "a", 1}
#  print (super_set)   True это 1 . False это 0
# выведет {True,"a"}
#########################################
# Если все элементы  истина или множество пустое all
# super_set = {"",0.00, False,  0,  "a",False, 1}
# print(all(super_set))
###############################################
#Возвращает True  если хоть 1 элемент истина any
# super_set = {"",0.00, False,  0,  "a",False, 1}
# # print(any(super_set))
############################################
# функция enumerate
# cool_set = {1,88,"audi",(1,2),0,'lada'}
# print(enumerate(cool_set))
# cool_set = {1,88,"audi",(1,2),0,'lada'}
# for index, value in enumerate(cool_set):
#     print(index,value)
#############################################
#добавление одного элемента метод add.Добавление нескольких элементов метод update
# cool_set = {1,88,"audi",(1,2),0,'lada'}
# cool_set.add(4)
# cool_set.update([3,4,5])
# print(cool_set)
####################################
#Удаление элементов из множества discard и remove (если удалять объект которого уже нет- вызовет ошибку метод строгий
# хотим убедится что мы точно что-то удалили.)
# cool_set = {0, 1, (1, 2), 4, 3, 5, 'lada', 88, 'audi'}
# cool_set.remove(3)
# print(cool_set)
# cool_set.discard(4)
# print(cool_set)
###########################################
# метод pop
# cool_set = {0, 1, (1, 2), 4, 3, 5, 'lada', 88, 'audi'}
# cool_set.pop()
# print(cool_set)
################################################
#как отсортировать множества ? sorted выдает список принтом. Добавляем вложенность sorted  выдает кортеж
# cool_set = {0, 1, 4, 3, 5, 88}
# print(sorted(cool_set))
# cool_set = {0, 1, 4, 3, 5, 88}
# print(tuple(sorted(cool_set)))
###############################################################
#итерируем множество. Все время разная последовательность
# cool_set = {0, 1, (1, 2), 4, 3, 5, 'lada', 88, 'audi'}
# for element in cool_set:
#     print(element)
###########################
#сравнение множеств
# set1= set("KION")
# set2 = set('INOK')
# set3 =set ("Super KION")
# set4 =set("Hello")
# #print(set1==set2
# # Подмножетва // Надмножеста
# print(set2 > set1)
# print(set3> set1) # set3 является надмножеством set1
# print(set2 < set3) # set2 является подмножеством set3
# print(set4> set3)
