class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:  # Проверка на нулевой знаменатель
            raise ValueError("Знаменатель не может быть равен 0")
        if not all(isinstance(val, (int, float)) for val in (numerator, denominator)):
            raise ValueError("Числитель и знаменатель должны быть числами")
        self._numerator = numerator
        self._denominator = denominator

    @property
    def full_name(self):
        """Выведение дроби через слеш в строке"""
        return f"{self._numerator}/{self._denominator}"

    def __eq__(self, other):  # Проверка равенства (==)
        # if  isinstance(other, Fraction):
        #     return NotImplemented
        return self._numerator * other._denominator == self._denominator * other._numerator

    def __ne__(self, other):  # Проверка неравенства (!=)
        # if  isinstance(other, Fraction):
        #     return NotImplemented
        return self._numerator * other._denominator != self._denominator * other._numerator


    def __lt__(self, other):  # Проверка "меньше" (<)
        # if  isinstance(other, Fraction):
        #     return NotImplemented
        return self._numerator * other._denominator < self._denominator * other._numerator

    def __gt__(self, other):  # Проверка "больше" (>)

        return self._numerator * other._denominator > self._denominator * other._numerator

    def __le__(self, other):  # Проверка "меньше или равно" (<=)

         return self < other or self == other

    def __ge__(self, other):  # Проверка "больше или равно" (>=)

         return self._numerator * other._denominator >= self._denominator * other._numerator

drob1 = Fraction(1,2)
drob2  =Fraction (5,2)
print(drob1<=drob2)
class New_class(Fraction):
   def __init__(self,numerator,denominator):
       super().__init__(numerator,denominator)

drob3 = New_class(1,5)
drob4 = New_class(1,5)
print(drob1 <=drob2)


