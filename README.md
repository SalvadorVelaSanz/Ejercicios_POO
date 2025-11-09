# Ejercicio 1 — Duration

Crear una clase inmutable `Duration` que represente duraciones (horas:minutos:segundos). Debe permitir:

- Crear duraciones:
    - Ejemplo:
        ```py
        t = Duration(10, 20, 56)
        ```
- Normalizar automáticamente los campos:
    - `(10, 62, 15)` debe guardarse como `(11, 2, 15)`.
- Valores por defecto (si no se indican son cero):
    ```py
    Duration()         # (0, 0, 0)
    Duration(34)       # (34, 0, 0)
    Duration(34, 15)   # (34, 15, 0)
    Duration(34, 61)   # (35, 1, 0)
    ```
- Comparaciones entre duraciones (`==`, `<`, `>`, etc.).
- Sumar y restar segundos.
- Sumar y restar duraciones entre sí.

---

# Ejercicio 2 — Fraction

Crear una clase `Fraction` para fracciones. Debe permitir:

- Crear fracciones indicando numerador y denominador:
    ```py
    f = Fraction(2, 3)
    ```
- No permitir denominador cero (validación).
- Simplificar automáticamente (por ejemplo, `2/4` == `1/2`).
- Operar entre fracciones: sumar, restar, multiplicar, dividir.
- Operar con enteros/floats también (por ejemplo `f + 1`, `5 * f`).
- Comparaciones: `==`, `<`, `<=`, `>`, `>=`, `!=`.
    - Ejemplo: `1/2` es igual a `2/4`.
    - Debe permitir comparaciones mixtas: `1 < Fraction(1, 2)`.

---

# Ejercicio 3 — Date

Crear una clase `Date` para manejar fechas. Debe permitir:

- Crear fechas válidas:
    ```py
    d = Date(17, 11, 2022)  # día, mes, año
    ```
- Validar fechas y rechazar entradas erróneas:
    - Ejemplos inválidos:
        ```py
        Date(78, -45, 0)
        Date(31, 6, 2022)   # junio tiene 30 días
        Date(29, 2, 2022)   # 2022 no es bisiesto
        ```
- Comparaciones entre fechas (`==`, `<`, `>`, etc.).
- Sumar y restar días a una fecha.
- Restar dos fechas (obtener diferencia en días).
- Obtener el día de la semana de una fecha.
