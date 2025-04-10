Są to klasy służące jako szablony, które definiują strukturę i wymuszone metody dla klas pochodnych, ale same nie mogą być inicjalizowane. Używają dekoratora `@abstractmethod` do oznaczenia metod, które muszą być zaimplementowane w klasach pochodnych.

??? - tip "Korzyści wynikające z wykorzystywania abstrakcyjnych klas nadrzędnych"
    - **Spójność** – wymusza implementację określonych metod.
    - **Reużywalność** – pozwala dzielić metody między klasami.
    - **Polimorfizm** – umożliwia jednolite używanie różnych klas.

```python
from abc import ABC, abstractmethod

class Zwierze(ABC):
    # Ta metoda jest abstrakcyjna,
    # wymagana jest jej implementacja w klasach pochodnych
    @abstractmethod
    def wydaj_dzwiek(self):
        pass

class Pies(Zwierze):
    def wydaj_dzwiek(self):
        return "Hau hau!"

class Kot(Zwierze):
    def wydaj_dzwiek(self):
        return "Miau miau!"
```
