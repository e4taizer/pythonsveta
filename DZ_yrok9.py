###################################
# nomer1
# element = input()
# set1=set()
# tekyshee_chislo = ""
# for char in element:
#     if char.isdigit():
#         tekyshee_chislo += char
#     else:
#         if tekyshee_chislo:
#             set1.add(int(tekyshee_chislo))
#             tekyshee_chislo = ""
# if tekyshee_chislo:
#     set1.add(int(tekyshee_chislo))
# sortirovanoe_mnogestvo = sorted(set1)
# dlina_mnogestwa = len(set1)
# if  dlina_mnogestwa % 2 ==1:
#   mediana =sortirovanoe_mnogestvo[dlina_mnogestwa// 2]
#   print(f"Медиана введенного множества:{mediana}")
# else:
#
#   print(f"Для четного количества елементов медиану рассчитать сложно")
#################################################################
#nomer2
# first={"KION","DSP","Music","Live","MTS bank"}
# second={"KION","Compliance","PPInfo"}
# third={"DSP","Cashback","PPInfo","service_desk"}
# unique_in_first = first - second - third
# unique_in_second = second - first - third
# unique_in_third = third - first - second
# for item in unique_in_first:
#     print(f"Только в first: {item}")
#
# for item in unique_in_second:
#     print(f"Только в second: {item}")
#
# for item in unique_in_third:
#     print(f"Только в third: {item}")
###############################################
# nomer3
# set1 =set()
# import random
# for element in range(20):
#     set1.add (random.randrange(1, 81, 1))
# bilet_loto =set()
# numbers = input(f"введите числа разделеные пробелами: ")
# for num in numbers.split():
#     bilet_loto.add(int(num))
# print (f"Введенные мной номера:{bilet_loto}")
# print(f"Выпавшие номера {set1}")
# sovpadenie = set1 & bilet_loto
# print(f"Проверяем совпадение чисел {sovpadenie}")
# if len(sovpadenie) == 5:
#     print(f"Бинго!! Вы только что сорвали джекпот!")
# if len(sovpadenie) == 4:
#     print(f"Вы выиграли электронный скутер и парилку!")
# if len(sovpadenie) == 3:
#     print(f"Вы виграли 20 рублей!")
# else:
#     print(f"Вы проиграли в игру 'Бинго'")
####################################################
###########Nomer4

first_day_failed =["test_auth.py", "test_show_case.py", "test_map.py", "test_map.py", "test_show_case.py", "test_shopping_cart.py"]
second_day_failed =["test_map.py", "test_geo.py", "test_func.py", "test_old.py", "test_old.py", "test_shopping_cart.py"]
third_day_failed =["test_old.py", "test_old.py", "test_shopping_cart.py", "test_shopping_cart.py", "test_shipment.py"]
ynikalnie_ypavshie_tests = set ()
for test_list in (first_day_failed,second_day_failed,third_day_failed):
    for item in test_list:
        ynikalnie_ypavshie_tests.add(item)
print(f"Уникальные: {ynikalnie_ypavshie_tests}")
obshee_kolichestvo_testov = 378
kolichestvo_ypavshix = len(first_day_failed) + len(second_day_failed) + len(third_day_failed)
fail_rate = kolichestvo_ypavshix/ obshee_kolichestvo_testov
if  fail_rate>= 3 :
    print(f"Требуется анализ ошибок. Файл рейт превышает  3% и составляет: {fail_rate}")
else:
    print(f"Можно деплоить в прод. Файл рейт  не превышает 3% и составляет: {fail_rate:.2f}%")