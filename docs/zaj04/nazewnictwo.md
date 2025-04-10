
Żeby otrzymać kod czytelny, spójny z innymi projektami i łatwy w utrzymaniu w zespole, wykorzystuje się konwencję nazewnictwa na podstawie PEP 8 (standard i przewodnik stylu w Pythonie). 

Najważniejsze konwencje:

1. Zmienne lokalne

    - **Styl:** `snake_case`  
    - **Przykład:** `total_count`  
    - **Opis:** Małe litery, słowa oddzielone podkreśleniem. Najczęściej używany styl.

2. Funkcje

    - **Styl:** `snake_case`  
    - **Przykład:** `calculate_average()`  
    - **Opis:** Nazwa opisowa, zawiera czasownik – mówi, co robi funkcja.

3. Klasy

    - **Styl:** `PascalCase`  
    - **Przykład:** `DataProcessor`  
    - **Opis:** Każde słowo wielką literą, bez podkreśleń. Stosowane też do wyjątków.

4. Stałe (np. konfiguracja)

    - **Styl:** `UPPER_CASE`  
    - **Przykład:** `MAX_BUFFER_SIZE = 1024`  
    - **Opis:** Duże litery, słowa oddzielone podkreśleniem. Stałe konfiguracyjne i wartości niezmienne.

    ```python
    # Stałe
    PI = 3.14159
    MAX_CONNECTIONS = 10
    DEFAULT_TIMEOUT = 30  # sekundy

    def calculate_circle_area(radius):
        return PI * radius**2

    print(f"Pole koła o promieniu 2: {calculate_circle_area(2)}")

    # Użycie stałych konfiguracyjnych
    def connect_to_server(timeout=DEFAULT_TIMEOUT):
        print(f"Łączenie z serwerem... (timeout: {timeout}s)")

    connect_to_server()
    ```

5. Nazwa modułów / plików

    - **Styl:** `snake_case`  
    - **Przykład:** `data_utils.py`  
    - **Opis:** Małe litery i podkreślenia. Nazwy powinny być krótkie i opisowe.

6. Nazwy pakietów

    - **Styl:** `lowercase`  
    - **Przykład:** `analytics`  
    - **Opis:** Zazwyczaj jedno słowo, wszystkie litery małe.

7. Prywatne zmienne lub funkcje - umowna konwencja

    - **Styl:** `_snake_case`  
    - **Przykład:** `_internal_use_only()`  
    - **Opis:** Jeden podkreślnik sugeruje, że dany element (zmienna, funkcja) jest przeznaczony wyłącznie do użytku wewnętrznego w module lub klasie. Nie są importowane przez `from module import *`.

    ```python
    _internal_variable = "prywatna zmienna"

    def _helper_function():
        return "wewnętrzna funkcja"
    ```

8. Naprawdę prywatne zmienne/metody (w klasie)

    - **Styl:** `__snake_case`  
    - **Przykład:** `__very_private`  
    - **Opis:** Aktywują mechanizm name mangling – Python przekształca nazwę wewnętrznie, aby uniknąć kolizji nazw w klasach dziedziczących. Najczęściej używane w klasach do oznaczania "naprawdę prywatnych" atrybutów lub metod.

    ```python
    class MyClass:
        def __init__(self):
            self.__private = 42  # Python zmienia to na _MyClass__private

    obj = MyClass()
    print(obj._MyClass__private)  # Dostęp nadal możliwy, ale nazwa została ukryta
    ```

9. Metody specjalne (magiczne)

    - **Styl:** `__dunder__`  
    - **Przykład:** `__init__`, `__str__`  
    - **Opis:** Metody specjalne używane przez interpreter. Nie tworzymy własnych nazw w tym stylu!