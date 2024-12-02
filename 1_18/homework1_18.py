class Fraction:
       def __init__(self,numerator,denominator):
              self.numerator = numerator
              self.denominator = denominator
              if self.denominator !=0:                       # проверка на то что не может быть 0  знаменатель
                     self.denominator =denominator
              else:
                     raise ValueError(f"Знаменатель дроби не может быть 0")

              if not all(isinstance(val, (int, float)) for val in (self.numerator, self.denominator)):
                     raise ValueError("Числитель и знаменатель должны быть числами")

       @property
       def full_name(self):                                           # выведение дроби через слеш в строке
             return f"{self.numerator}/{self.denominator}"

       def __getattr__(self, name):                                   #  обращение к  не существующему атрибуту класса
                return "У дробных чисел нет такого атрибута: {}".format(name)



# new_fraction =Fraction(5,2)
# print(new_fraction.full_name)
       @classmethod

       def create_fraction_from_int(cls,new_number):                             # создание объекта из целого числа
             return cls(new_number,1)

       @classmethod

       def create_fraction_from_float(cls, value):                               # создание объекта из флоат
           denominator = 1000
           numerator = int(value * denominator)
           return cls(numerator, denominator)
       # @property
       # def numerator(self):
       #     """Геттер для числителя"""
       #     return self._numerator

       # @numerator.setter
       # def numerator(self,value):
       #     """Сеттер для числителя. Возвращает новый экземпляр с новым числителем."""
       #     if not isinstance(value, (int, float)):
       #         raise ValueError("Числитель должен быть числом")
       #     return Fraction(value, self._denominator)                              #self._numerator = value

       # @property
       # def denominator(self):
       #     """Геттер для знаменателя."""
       #     return self._denominator
       # @denominator.setter

       # def denominator(self, value):
       #     """Сеттер для знаменателя. Возвращает новый экземпляр с новым знаменателем."""
       #     if value == 0:
       #         raise ValueError("Знаменатель не может быть равен 0")
       #     if not isinstance(value, (int, float)):
       #         raise ValueError("Знаменатель должен быть числом")
       #     return Fraction(self._numerator,value)



drob1 = Fraction(1,2)
#print(drob1.full_name,{drob1})
drob2 = Fraction(3,4)
#print(drob2.full_name)
drob3= Fraction(4,12)
#print(drob3.full_name)
drob4=Fraction.create_fraction_from_float(2.3)
#print(drob4.full_name)
drob5=Fraction.create_fraction_from_int(10)
drob6 = Fraction(1,4)
drob7 = Fraction(4, 4)
drob8 = Fraction(1, 4)

print(drob5.full_name)
print(drob5.test)                                                               # проверка обращения к не существующему атрибуту
print(drob1.full_name)
drob1.numerator = 5
print(drob1.full_name)



fraction = Fraction.create_fraction_from_float(1.789)
print(f"Числитель: {fraction.numerator}, Знаменатель: {fraction.denominator}")

#fraction = Fraction.create_fraction_from_int(5)
#print(f"Числитель: {fraction.numerator}, Знаменатель: {fraction.denominator}")

class Сomputation_with_fractions(Fraction):
    def __add__ (self,other):                                                          #Метод для сложения дробей
        if isinstance(self,Fraction):
            if not isinstance(self, Сomputation_with_fractions):   # проверка и преобразование что селф не является экземпляром класа Вычисление, и преобразование в этот класс
                self = Сomputation_with_fractions(self.numerator, self.denominator)
            if not isinstance(other, Сomputation_with_fractions): # проверка и преобразование что other не является экземпляром класа Вычисление, и преобразование в этот класс
                other = Сomputation_with_fractions(other.numerator, other.denominator)
            common_denominator = self.denominator * other.denominator
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            return Сomputation_with_fractions(new_numerator, common_denominator)
        else:
            raise ValueError ("Операция сложения возможна только с объектами Fraction или его подклассов")
#result = Сomputation_with_fractions(drob2.numerator, drob2.denominator) + drob5
#print(result.full_name)

    def __sub__(self, other):                                           # Метод для вычитания
       if not isinstance(other, Fraction):
           raise ValueError("Операция вычитания возможна только с объектами Fraction или его подклассов")

       if not isinstance(self, Сomputation_with_fractions):
          self = Сomputation_with_fractions(self.numerator, self.denominator)

       if not isinstance(other, Сomputation_with_fractions):
            other = Сomputation_with_fractions(other.numerator, other.denominator)

    # Случай 1: знаменатели одинаковы
       if self.denominator == other.denominator:
             if self.numerator >= other.numerator:
                 new_numerator = self.numerator - other.numerator
                 return Сomputation_with_fractions(new_numerator, self.denominator)
             else:
                 raise ValueError("Числитель первой дроби должен быть больше или равен числителю второй дроби")

    # Случай 2: знаменатели разные
       common_denominator = self.denominator * other.denominator
       new_numerator_self = self.numerator * other.denominator
       new_numerator_other = other.numerator * self.denominator

       if new_numerator_self >= new_numerator_other:
            new_numerator = new_numerator_self - new_numerator_other
            return Сomputation_with_fractions(new_numerator, common_denominator)
       else:
            raise ValueError(f"После приведения дробей числитель первой дроби должен быть больше или равен числителю второй дроби")

drob10 = Fraction(5, 10)
drob11 = Fraction(10, 20)

#result = Сomputation_with_fractions(drob10.numerator, drob10.denominator) - drob11

#print(result.full_name)
class Delenie(Fraction):
     def __truediv__(self, other):                                        # деление

        if not isinstance(other, Fraction):
           raise ValueError("Операция деления возможна только с объектами Fraction или его подклассов")

        if not isinstance(self, Delenie):
           self = Delenie(self.numerator, self.denominator)

        if not isinstance(other, Delenie):
            other = Delenie(other.numerator, other.denominator)
        if  self.denominator == 0 or other.denominator ==0:
           raise ValueError("В знаменателе дроби находится 0, это ошибка!")
        new_numerator = self.numerator*other.denominator
        new_denominator = self.denominator*other.numerator
        return Delenie(new_numerator,new_denominator)

drob12 = Fraction(5,7)
drob13 = Fraction(10,50)
result = Delenie(drob12.numerator,drob12.denominator) / drob13
#print(result.full_name)
class Ymnojenie(Fraction):
   def __mul__(self, other):
      if not isinstance(other, Fraction):
          raise ValueError("Операция умножения возможна только с объектами Fraction или его подклассов")

      if not isinstance(self, Ymnojenie):
          self = Ymnojenie(self.numerator, self.denominator)

      if not isinstance(other, Ymnojenie):
          other = Ymnojenie(other.numerator, other.denominator)

      new_numerator = self.numerator * other.numerator
      new_denominator = self.denominator * other.denominator
      return Ymnojenie(new_numerator,new_denominator)
result = Ymnojenie(drob12.numerator,drob12.denominator) * drob13
#print(result.full_name)
class Sravnenie(Fraction):                                                         # с  объектами классом Fraction  работают только 2 первых метода, остальные работают только  в классе Sravnenie
                            # не сравнивается 2 объекта класса  Fraction  между собой всеми методами кроме первых двух
                            # причем  проверки проходят если сравнивается один объект Fraction  и объект Sravnenie
    def __eq__(self, other):  # Проверка равенства (==)
        # if  isinstance(other, Fraction):
        #     return NotImplemented
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other):  # Проверка неравенства (!=)
        # if  isinstance(other, Fraction):
        #     return NotImplemented
        return self.numerator * other.denominator != self.denominator * other.numerator


    def __lt__(self, other):  # Проверка "меньше" (<)
        # if  isinstance(other, Fraction):
        #     return NotImplemented
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other):  # Проверка "больше" (>)
        # if  isinstance(other, Fraction):
        #     return NotImplemented
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __le__(self, other):  # Проверка "меньше или равно" (<=)
        # if  isinstance(other, Fraction):
        #     return NotImplemented
        return self < other or self == other

    def __ge__(self, other):  # Проверка "больше или равно" (>=)
        # if  isinstance(other, Fraction):
        #     return NotImplemented
        return self > other or self == other

drob15 = Sravnenie(1, 2)
drob16 = Sravnenie(3, 4)
print(drob1 < drob2)         # не работает оба  объекта класса Fraction
print(drob15>drob16)            # а этот работает один объект Fraction  другой Sravnenie













