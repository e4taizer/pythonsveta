#Наследование
###### super
# class Parent:
#     def __init__(self):
#         self.parent_name ="Sergey"
#         print("Родительский класс отработал")
#
# class Child(Parent):
#     def __init__(self):
#       super().__init__()
#       self.child_name = "Vova"
#       print("Детский класс отработал")
#
#
# child = Child()
# print(child.parent_name)
###############
#множественное наследование
# class Parent:
#     def walk(self):
#         print("parent walking")
#
#
# class Child(Parent):
#     def walk(self):
#         print("child walking")
# class GrandChild(Parent,Child):
#     pass
# grand_child = GrandChild()
# grand_child.walk()
#############################
##Исключения
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[11])






