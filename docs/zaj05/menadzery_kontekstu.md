Są to narzędzia, które pomagają w **zarządzaniu zasobami**, takimi jak pliki, połączenia sieciowe, czy połączenia z bazami danych. Dzięki menadżerom kontekstu można upewnić się, że zasoby zostaną poprawnie otwarte, a następnie zamknięte – nawet jeśli w trakcie korzystania z zasobu wystąpi wyjątek.

## Instrukcja `with`

Python zapewnia obsługę menadżerów kontekstu za pomocą instrukcji `with`, która gwarantuje poprawne zarządzanie zasobami. Gdy używamy `with`, zasób jest automatycznie otwierany i zamykany, co zmniejsza ryzyko wycieków pamięci i innych błędów wynikających z niezamknięcia zasobów.

```python
with open("plik.txt", "w") as plik:
    plik.write("Witaj, świecie!")
```

## Tworzenie własnych menadżerów kontekstu

Aby utworzyć własny menadżer kontekstu, wystarczy zdefiniować klasę z dwiema metodami:

- `__enter__` – ta metoda jest wywoływana na początku bloku `with` i powinna zwracać zasób, którym będziemy zarządzać.
- `__exit__` – ta metoda jest wywoływana na końcu bloku `with` i służy do czyszczenia zasobu (np. zamknięcia go), bez względu na to, czy wystąpił wyjątek.

Jako przykład, menadżer kontekstu dla połączenia z bazą danych:

```python
class PolaczenieBazaDanych:
    def __enter__(self):
        print("Nawiązywanie połączenia z bazą danych...")
        # Symulacja połączenia, np. self.conn = connect_to_database()
        self.polaczenie = "Połączenie aktywne"
        return self.polaczenie

    def __exit__(self, exc_type, exc_value, traceback):
        print("Zamykanie połączenia z bazą danych...")
        # Symulacja zamknięcia połączenia, np. self.conn.close()
        self.polaczenie = None

# Użycie menadżera kontekstu
with PolaczenieBazaDanych() as polaczenie:
    print(polaczenie)
    # Wykonanie operacji na bazie danych
```

### Obsługa wyjątków w `__exit__`

Metoda `__exit__` otrzymuje trzy argumenty: `exc_type`, `exc_value` i `traceback`, które są związane z wyjątkiem, który mógł wystąpić wewnątrz bloku `with`. Możemy dzięki nim obsłużyć wyjątek wewnątrz `__exit__` lub po prostu pozwolić, aby wyjątek został propagowany dalej.

```python
class PolaczenieBazaDanych:
    def __enter__(self):
        print("Nawiązywanie połączenia z bazą danych...")
        self.polaczenie = "Połączenie aktywne"
        return self.polaczenie

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Wystąpił wyjątek: {exc_value}")
        print("Zamykanie połączenia z bazą danych...")
        self.polaczenie = None

# Użycie menadżera kontekstu z wyjątkiem
try:
    with PolaczenieBazaDanych() as polaczenie:
        print(polaczenie)
        raise ValueError("Symulowany błąd!")
except ValueError:
    print("Obsłużono wyjątek!")
```