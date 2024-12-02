class Animalnew:
    "Это класс не просто так!"
    paws_count = 4
    type = "pet"
    def __init__(self,head = "круглый"):
        print("Мы в имите")
        self.tail = 0
        self.head=head
    def set_animal_type(self):
        print("Это мы меняем тип животного"+str(self))
def set_tail_lenght(self,l):
    self.tail =l
def __del__(self):
    print("Мення пытаются убить!")
# animal_1=Animalnew()
# type(animal_1)
# isinstance(animal_1,Animalnew)
# Animalnew.type = "wild"
# animal_2 = Animalnew()
# Animalnew.type ="pet"
# animal_1.type="wild"
# Animalnew.type = "testtest"
# animal_1.__dict__
# animal_1.__dict__
# {'type': 'wild'}
# animal_2.__dict__
# {}
# animal_2.paws_count = 2
# animal_2.__dict__
# {'paws_count': 2}