import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator // math.gcd(numerator, denominator)
        self.denominator = denominator // math.gcd(numerator, denominator)

    def __add__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("incorrect type")
        if isinstance(other, int):
            result_numerator = self.numerator + self.denominator * other
            result = Rational(result_numerator, self.denominator)

        result_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Rational(result_numerator, result_denominator)


    def __iadd__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("incorrect type")
        if isinstance(other, int):
            other = Rational(other)
        result_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        result_denominator = self.denominator * other.denominator
        self.numerator = result_numerator // math.gcd(result_numerator, result_denominator)
        self.denominator = result_denominator // math.gcd(result_numerator, result_denominator)
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("incorrect type")
        if isinstance(other, int):
            other = Rational(other)
        result_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Rational(result_numerator, result_denominator)

    def __isub__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("incorrect type")
        if isinstance(other, int):
            other = Rational(other)
        result_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        result_denominator = self.denominator * other.denominator
        self.numerator = result_numerator // math.gcd(result_numerator, result_denominator)
        self.denominator = result_denominator // math.gcd(result_numerator, result_denominator)
        return self

    def __mul__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("incorrect type")
        if isinstance(other, int):
            other = Rational(other)
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Rational(result_numerator, result_denominator)

    def __imul__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("incorrect type")
        if isinstance(other, int):
            other = Rational(other)
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        self.numerator = result_numerator // math.gcd(result_numerator, result_denominator)
        self.denominator = result_denominator // math.gcd(result_numerator, result_denominator)
        return self

    def __truediv__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("incorrect type")
        if isinstance(other, int):
            other = Rational(other)
        result_numerator = self.numerator * other.denominator
        result_denominator = self.denominator * other.numerator

        return Rational(result_numerator, result_denominator)

    def __itruediv__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("incorrect type")
        if isinstance(other, int):
            other = Rational(other)
        result_numerator = self.numerator * other.denominator
        result_denominator = self.denominator * other.numerator
        self.numerator = result_numerator // math.gcd(result_numerator, result_denominator)
        self.denominator = result_denominator // math.gcd(result_numerator, result_denominator)
        return self

    def __eq__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("incorrect type")
        if isinstance(other, int):
            other = Rational(other)
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other):
        """self < other"""
        if not isinstance(other, (int, Rational)):
            raise TypeError("incorrect type")
        if isinstance(other, int):
            other = Rational(other)
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other):
        """self > other"""
        if not isinstance(other, (int, Rational)):
            raise TypeError("incorrect type")
        if isinstance(other, int):
            other = Rational(other)
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __str__(self):
        """Return a reduced fraction"""
        return f'{self.__numerator}/{self.__denominator}'

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError("Incorrect data")
        self.__numerator = numerator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise TypeError("Incorrect data")
        if not denominator:
            raise ZeroDivisionError("Incorrect data")
        self.__denominator = denominator


obj1 = Rational(1, 5)
obj2 = Rational(3, 5)
print(obj1 + obj2)
print(obj1 + 5)
obj1 += obj2
print(obj1)
print(obj1 - obj2)
print(obj1 - 5)
obj1 -= 3
print(obj1)
print(obj1 * obj2)
print(obj2 * 5)
obj1 *= 3
print(obj1)
print(obj1 / obj2)
print(obj2 / 5)
obj1 /= obj2
print(obj1)
print(obj1 == obj2)
print(obj1 < obj2)
print(obj1 > obj2)
