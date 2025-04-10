### Metody instancji

Domyślny sposób działania, jako pierwszy argument przyjmują `self`, który odnosi się do instancji.

!!! tip "Zastosowanie: operacje na instancji"

### Metody klasy

Deklarowane za pomocą dekoratora `@classmethod`. Przyjmują jako pierwszy argument `cls`, który odnosi się do samej klasy, a nie jej instancji.

```python
class Pracownik:
    liczba_pracownikow = 0  # Atrybut klasy

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        Pracownik.liczba_pracownikow += 1

    @classmethod
    def z_nazwiska(cls, nazwisko):
        # Alternatywny konstruktor
        return cls(nazwisko, 'Nieznane stanowisko')

    @classmethod
    def ustaw_liczbe_pracownikow(cls, liczba):
        cls.liczba_pracownikow = liczba

# Tworzenie instancji za pomocą metody klasy
nowy_pracownik = Pracownik.z_nazwiska('Kowalski')
print(nowy_pracownik.imie)           # Kowalski
print(nowy_pracownik.stanowisko)     # Nieznane stanowisko
```

!!! tip "Zastosowanie: operacje na klasie, alternatywne konstruktory"

### Metody statyczne

Deklarowane za pomocą dekoratora `@staticmethod`. Nie przyjmują żadnego specjalnego pierwszego argumentu i nie mają dostępu ani do instancji (`self`), ani do klasy (`cls`).

```python
class Kalkulator:
    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b

# Wywoływanie metod statycznych
print(Kalkulator.dodaj(5, 3))     # 8
print(Kalkulator.odejmij(10, 4))  # 6
```

!!! tip "Zastosowanie: funkcje pomocnicze powiązane tematycznie"

### 📝 Zadanie

Zapoznaj się z metodami w klasie z `geoapps.zajecia03.fleet.ambulance`.