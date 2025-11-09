class Duration:

    #Inicializa la duración con horas, minutos y segundos por defecto son 0 .
    def __init__ (self, hours=0, minutes = 0, seconds = 0):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        if total_seconds < 0:
            raise ValueError("La duracion no puede ser negativa")

        self._hours = total_seconds // 3600
        remainder = total_seconds % 3600
        self._minutes = remainder // 60
        self._seconds = remainder % 60

    # Propiedades para acceder a horas, minutos y segundos
    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes

    @property
    def seconds(self):
        return self._seconds

    #Método para representar la duración como una cadena
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    #Método para convertir la duración a segundos
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    #Método de clase para crear una duración a partir de segundos (No es necesario que sea de clase, se puede poner normal)
    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        remainder = total_seconds % 3600
        minutes = remainder // 60
        seconds = remainder % 60
        return cls(hours, minutes, seconds)

    #Metódos de comparación
    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()
    
    #Métodos para sumar y restar segundos
    
    def add_seconds(self, seconds):
        return Duration.from_seconds(self.to_seconds() + seconds)

    def sub_seconds(self, seconds):
        total = self.to_seconds() - seconds
        if total < 0:
            raise ValueError("La duración no puede ser negativa")
        return Duration.from_seconds(total)

    #Métodos para sumar y restar duraciones

    def __add__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return Duration.from_seconds(self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        total = self.to_seconds() - other.to_seconds()
        if total < 0:
            raise ValueError("La duración no puede ser negativa")
        return Duration.from_seconds(total)


def main():
    #Pruebas de la clase Duration
    duracion1 = Duration(1, 30, 45)
    duracion2 = Duration(0, 45, 30)

    print("Duracion 1:", duracion1)
    print("Duracion 2:", duracion2)

    suma = duracion1 + duracion2
    resta = duracion1 - duracion2

    print("Suma:", suma)
    print("Resta:", resta)

    print("Duracion 1 en segundos:", duracion1.to_seconds())
    print("Duracion 2 en segundos:", duracion2.to_seconds())

if __name__ == "__main__":
    main()    