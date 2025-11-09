from math import gcd

class Fraction:

    #constructor que simplifica la fraccion al crearla usando gcd

    def __init__(self, numerator, denominator=1):

        if denominator == 0:
            raise ValueError("El denominador no puede ser 0")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        common = gcd(numerator,denominator)


        self.numerator = numerator // common
        self.denominator = denominator // denominator

    #propiedades para obtener numerador y denominador

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator
    
    #string

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    

    #operaciones usando las formulas de fracciones

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)

        #(a/b)+(c/d)=(a*d + b*c / b*d)

        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)

         #(a/b)-(c/d)=(a*d - b*c / b*d)
  
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __rsub__(self, other):
        return Fraction(other) - self

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        
        #(a/b)*(c/d)=(a*c / b*d)
    
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)


        #(a/b)/(c/d)=(a*d / b*c)
    
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)

    def __rtruediv__(self, other):
        return Fraction(other) / self



    #comparaciones

    # se usa la formula del factor cruzado para las comparaciones: a*d == b*c ...

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return (self.numerator * other.denominator ==
                other.numerator * self.denominator)

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return (self.numerator * other.denominator <
                other.numerator * self.denominator)

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other
    


def main():
    #Pruebas de la clase Fraction

    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)

    print(f1 + f2)     # 5/4
    print(f1 * 2)      # 1/1
    print(2 * f1)      # 1/1
    print(1 + f1)      # 3/2
    print(1 < f1)      # False
    print(f1 < 1)      # True
    print(f1 == Fraction(2, 4))  # True




if __name__ == "__main__":
    main()    
    