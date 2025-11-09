class Date:

    #Constantes de la clase
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    WEEKDAYS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    #Constructor que valida que la fecha sea correcta
    def __init__(self, day, month, year):
        if not self._is_valid_date(day, month, year):
            raise ValueError("Fecha no válida")
        self._day = day
        self._month = month
        self._year = year

    #Propiedades para obtener día, mes y año
    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    def __str__(self):
        return f"{self.day:02}/{self.month:02}/{self.year}"


    #Validación de fechas

    #Método estático para verificar si un año es bisiesto
    @staticmethod
    def _is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    #classmethod para usar en validacion de dias por mes

    @classmethod
    def _days_in_month(cls, month, year):
        if month == 2 and cls._is_leap_year(year):
            return 29
        return cls.DAYS_IN_MONTH[month - 1]


    @classmethod
    def _is_valid_date(cls, day, month, year):
        if year <= 0 or month < 1 or month > 12 or day < 1:
            return False
        if day > cls._days_in_month(month, year):
            return False
        return True

  
    #Operaciones con fechas
    #Convierte la fecha a un número de días desde el año 1.

    def to_ordinal(self):
        days = self.day
        for m in range(1, self.month):
            days += self._days_in_month(m, self.year)
        # Suma los días de los años anteriores
        for y in range(1, self.year):
            days += 366 if self._is_leap_year(y) else 365
        return days

    #Crea una fecha a partir del número de días desde el año 1.

    @classmethod
    def from_ordinal(cls, ordinal):
        year = 1
        while True:
            days_in_year = 366 if cls._is_leap_year(year) else 365
            if ordinal > days_in_year:
                ordinal -= days_in_year
                year += 1
            else:
                break

        month = 1
        while True:
            dim = cls._days_in_month(month, year)
            if ordinal > dim:
                ordinal -= dim
                month += 1
            else:
                break

        day = ordinal
        return cls(day, month, year)

    #Operaciones con fechas

    def __add__(self, days):
        if not isinstance(days, int):
            raise TypeError("Solo se pueden sumar días (int)")
        return Date.from_ordinal(self.to_ordinal() + days)

    def __sub__(self, other):
        if isinstance(other, Date):
            return self.to_ordinal() - other.to_ordinal()
        elif isinstance(other, int):
            return Date.from_ordinal(self.to_ordinal() - other)
        else:
            raise TypeError("Solo se puede restar otra fecha o un número de días")


    #Comparaciones de fechas

    def __eq__(self, other):
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)

    def __lt__(self, other):
        return self.to_ordinal() < other.to_ordinal()

    def __le__(self, other):
        return self.to_ordinal() <= other.to_ordinal()

    def __gt__(self, other):
        return self.to_ordinal() > other.to_ordinal()

    def __ge__(self, other):
        return self.to_ordinal() >= other.to_ordinal()

    def __ne__(self, other):
        return not self.__eq__(other)


    #Día de la semana

    def weekday(self):
        #Algoritmo de Zeller para calcular el día de la semana
        d, m, y = self.day, self.month, self.year
        if m < 3:
            m += 12
            y -= 1
        k = y % 100
        j = y // 100
        h = (d + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7
        # En Zeller: 0 = sábado ... 6 = viernes
        return self.WEEKDAYS[(h + 5) % 7]

#Pruebas de la clase Date

def main():
    f1 = Date(17, 11, 2022)
    f2 = Date(20, 11, 2022)

    print(f1)                   # 17/11/2022
    print(f1.weekday())         # jueves
    print(f1 + 10)              # 27/11/2022
    print(f2 - f1)              # 3 (días de diferencia)
    print(f1 < f2)              # True
    print(f1 - 5)               # 12/11/2022


if __name__ == "__main__":
    main()    
