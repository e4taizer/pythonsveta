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

    @property
    def numerator(self):
        """Геттер для числителя"""
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        """Сеттер для числителя. Создает новый объект с новым числителем."""
        if not isinstance(value, (int, float)):
            raise ValueError("Числитель должен быть числом")
        self._denominator = value

    def with_new_numerator(self, value):
        """Создает новый объект с заданным числителем."""
        if not isinstance(value, (int, float)):
            raise ValueError("Числитель должен быть числом")
        return Fraction(value, self._denominator)

    @property
    def denominator(self):
        """Геттер для знаменателя"""
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        """Сеттер для знаменателя. Создает новый объект с новым знаменателем."""
        if value == 0:
            raise ValueError("Знаменатель не может быть равен 0")
        if not isinstance(value, (int, float)):
            raise ValueError("Знаменатель должен быть числом")
        self._numerator = value

    def with_new_denominator(self, value):
        """Создает новый объект с заданным знаменателем."""
        if value == 0:
            raise ValueError("Знаменатель не может быть равен 0")
        if not isinstance(value, (int, float)):
            raise ValueError("Знаменатель должен быть числом")
        return Fraction(self._numerator, value)


# Пример использования:
drob1 = Fraction(3, 4)
print(drob1.full_name)  # 3/4

# Создание нового объекта с новым числителем:
new_drob1 = drob1.with_new_numerator(10)
print(new_drob1.full_name)

# Создание нового объекта с новым знаменателем:
new_drob2 = drob1.with_new_denominator(10)
print(new_drob2.full_name)

# Исходный объект не изменяется:
print(drob1.full_name)  # 3/4



class Compare_fraction(Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)
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

        return self._numerator * other._denominator <= self._denominator * other._numerator

    def __ge__(self, other):  # Проверка "больше или равно" (>=)

        return self._numerator * other._denominator >= self._denominator * other._numerator  # return self > other or self == other


drob3 = Compare_fraction(5, 10)
drob4 = Compare_fraction(11, 12)
print(new_drob2>=drob3)  # сравнивается 1 объект из главного класса, другой из родительского
print(drob3<=drob4)
print(drob1>new_drob2) # не сравнивает 2 объкта  главного класса методами >  <  >=  <=, но почему то сравнивает == и !=