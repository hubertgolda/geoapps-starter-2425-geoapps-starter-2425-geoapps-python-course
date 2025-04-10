Może być przydatne, gdy chcemy dodać dodatkową funkcjonalność lub dostosować zachowanie istniejących typów (np. `list`, `dict`, `str`) do specyficznych potrzeb projektu.

### Za pomocą osadzania (kompozycja)

Poprzez utworzenie nowej klasy, która wewnętrznie przechowuje instancję typu wbudowanego jako atrybut.

W ten sposób klasa ta może wykorzystywać typ wbudowany i rozszerzać jego funkcjonalność, delegując operacje na ten typ, ale nie dziedziczy jego metod bezpośrednio. Osadzanie jest przydatne, gdy chcemy dodać now funkcje bez ingerencji w istniejące metody typu wbudowanego.

```python
class MojaLista:
    def __init__(self, elementy):
        self._lista = elementy  # Osadzenie typu wbudowanego list

    def suma(self):
        return sum(self._lista)

    def dodaj(self, element):
        self._lista.append(element)

    def __str__(self):
        return str(self._lista)

moja_lista = MojaLista([1, 2, 3])
moja_lista.dodaj(4)
print(moja_lista)        # [1, 2, 3, 4]
print(moja_lista.suma()) # 10
```

### Za pomocą klas podrzędnych (dziedziczenia)

Poprzez utworzenie klasy podrzędnej, która dziedziczy po typie wbudowanym. Dzięki temu klasa podrzędna automatycznie przejmuje wszystkie metody i atrybuty typu bazowego, co pozwala na łatwe dodanie nowych funkcji lub nadpisanie istniejących metod.

```python
class MojaLista(list):
    def suma(self):
        return sum(self)

moja_lista = MojaLista([1, 2, 3, 4])
print(moja_lista)         # [1, 2, 3, 4]
print(moja_lista.suma())  # 10
```

### Za i przeciw

??? - tip "Za i przeciw dla obu sposobów"
    |               | Za                                                                                                                                                                                                                                   | Przeciw                                                                                                                                                                                                                                                                                                                                |
    | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Osadzanie     | Daje pełną kontrolę nad metodami, które są dostępne dla użytkownika klasy. Izoluje funkcjonalność rozszerzonego typu od interfejsu klasy bazowej, co może zwiększyć bezpieczeństwo i ułatwić utrzymanie kodu.                        | Wymaga ręcznego implementowania delegacji metod, jeśli potrzebujemy pełnego dostępu do funkcji typu wbudowanego. Może być mniej wydajne i bardziej czasochłonne niż dziedziczenie, jeśli chcemy używać większości metod typu wbudowanego.                                                                                            |
    | Dziedziczenie | Klasa pochodna automatycznie przejmuje wszystkie metody typu wbudowanego, co ułatwia tworzenie nowych funkcji. Jest bardziej ekonomiczne i intuicyjne w implementacji, szczególnie gdy potrzebujemy tylko kilku dodatkowych funkcji. | Trudniej jest zmodyfikować sposób działania niektórych metod w typach wbudowanych, ponieważ metody te mogą wywoływać bezpośrednie operacje na strukturze danych. Dziedziczenie może prowadzić do problemów z nieoczekiwanym zachowaniem, jeśli metody typu wbudowanego nie są dobrze przystosowane do nowych funkcji klasy pochodnej. |
