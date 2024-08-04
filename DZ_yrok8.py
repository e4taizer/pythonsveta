##### dz #1
# element = int(input())
# numbers = []
# if element % 2 ==0:
#  for i in range(2,element+1):
#      if i %2 ==0:
#          numbers.append(i)
#  print(numbers)
# elif  element % 2 != 0:
#  for i in range (1,element+1):
#      if i  % 2 != 0:
#          numbers.append(i)
#  print(numbers)
############################
#dz #2
# spisok = input()
# razdelenie = spisok.split('/')
# position = razdelenie.pop(-1)
# print(position)
##############################
# dz#3
# element = input()
# numbers = []
# current_number = ""
# for char in element:
#     if char.isdigit():
#         current_number += char
#     elif current_number:
#         numbers.append(int(current_number))
#         current_number = ''
# if current_number:
#   numbers.append(int(current_number))
#
#   chetnie = [num for num in numbers if num % 2 == 0]
#   chetnie = list(set(chetnie))
#   chetnie.sort()
#   ne_chetnie  =[num2 for num2 in numbers if num2 % 2 != 0]
#   ne_chetnie =  list(set(ne_chetnie))
#   ne_chetnie.sort()
#
# print(chetnie)
# print(ne_chetnie)
#########################################################
#dz#4
# element = input()
# numbers = []
# tekyshee_chislo = ""
#
# for char in element:
#     if char.isdigit():
#         tekyshee_chislo += char
#     else:
#         if tekyshee_chislo:
#             numbers.append(int(tekyshee_chislo))
#             tekyshee_chislo = ""
#
# if tekyshee_chislo:
#     numbers.append(int(tekyshee_chislo))
# if numbers:
#     max_chislo= max(numbers)
#     max_nomer_chisla = numbers.index(max_chislo)
# print(max_chislo)
# print(max_nomer_chisla)
####################################################################
#dz#5
# element = input()
# numbers = []
# tekyshee_chislo = ""
#
# for char in element:
#     if char.isdigit():
#         tekyshee_chislo += char
#     else:
#         if tekyshee_chislo:
#             numbers.append(int(tekyshee_chislo))
#             tekyshee_chislo = ""
#
# if tekyshee_chislo:
#     numbers.append(int(tekyshee_chislo))
# if numbers:
#     max_chislo = max(numbers)
#     min_chislo  =min(numbers)
#     max_index_chisla =numbers.index(max_chislo)
#     min_index_chisla = numbers.index(min_chislo)
#     numbers[max_index_chisla], numbers[min_index_chisla] = numbers[min_index_chisla], numbers[max_index_chisla]
# print(numbers)
######################################################################
#dz#7
# my_tuple1 =("спасибо","за",["лекции","занятия","поддержка","понимание"])
# my_tuple2 =("Даня","Александр","Владимир","Игорь")
# imia = my_tuple2[0]
# print(my_tuple2[0],",",my_tuple1[0], my_tuple1[1], my_tuple1[2][1])
# print(f"{my_tuple2[1]}, {my_tuple1[0]} {my_tuple1[1]} {my_tuple1[2][3]}.")


