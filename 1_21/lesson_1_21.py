############# коллекции модуль коллектионс
# from collections import Counter
# counter1 = Counter(a=2,b=0)
# counter2 = Counter(a=2)
# print(counter1==counter2)   # ,будут равны 2 объекта если в одном 0 , а в другом аргументе сходится
####################
# словарь defaultdict
# from collections import defaultdict
# first_dict = defaultdict(int)
# print(int())
# first_dict ["2"]
# print(first_dict)
# print(dict(first_dict)==first_dict)
#######
# from collections import Counter
# counter3= Counter(a =2)
# counter1 = Counter(a=2,b=0)
# print(counter1.__eq__({'a':2}))
########################## orderdict
# from collections import OrderedDict
# tests_ordered_dict = OrderedDict({'a':1,'b':2})
# print(tests_ordered_dict)
# second_ordered_dict = OrderedDict({'a':1,'b':2})
# print(tests_ordered_dict ==second_ordered_dict) # сравнивает с учетом порядка элементов, если поменять местами а и б будет фалсе
#######################двух стороняя очереть deque